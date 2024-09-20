#include <JuceHeader.h>

class MainComponent : public juce::Component
{
public:
    MainComponent()
    {
        // Initialise AudioDeviceManager (no input channels, 2 output channels)
        audioDeviceManager.initialise(0, 2, nullptr, true);
        
        // List input and output devices
        listAudioDevices();
    }

    void listAudioDevices()
    {
        // Get available audio devices
        auto deviceTypes = audioDeviceManager.getAvailableDeviceTypes();
        
        for (auto* deviceType : deviceTypes)
        {
            // Print device type (CoreAudio, ASIO, etc.)
            juce::Logger::outputDebugString("Device Type: " + deviceType->getTypeName());
            
            // Print input devices
            juce::StringArray inputDevices = deviceType->getDeviceNames(true);
            juce::Logger::outputDebugString("Input Devices:");
            for (const auto& inputDevice : inputDevices)
                juce::Logger::outputDebugString("  " + inputDevice);
            
            // Print output devices
            juce::StringArray outputDevices = deviceType->getDeviceNames(false);
            juce::Logger::outputDebugString("Output Devices:");
            for (const auto& outputDevice : outputDevices)
                juce::Logger::outputDebugString("  " + outputDevice);
        }
    }

private:
    juce::AudioDeviceManager audioDeviceManager;
};

class Application : public juce::JUCEApplication
{
public:
    const juce::String getApplicationName() override { return "List Audio Devices"; }
    const juce::String getApplicationVersion() override { return "1.0"; }
    
    void initialise (const juce::String&) override
    {
        mainWindow.reset(new MainWindow("List Audio Devices", new MainComponent(), *this));
    }

    void shutdown() override { mainWindow = nullptr; }

private:
    class MainWindow : public juce::DocumentWindow
    {
    public:
        MainWindow (juce::String name, juce::Component* c, JUCEApplication& a)
            : DocumentWindow (name, juce::Desktop::getInstance().getDefaultLookAndFeel()
                                .findColour (ResizableWindow::backgroundColourId),
                              DocumentWindow::allButtons), app(a)
        {
            setUsingNativeTitleBar (true);
            setContentOwned (c, true);
            setResizable (true, true);
            centreWithSize (getWidth(), getHeight());
            setVisible (true);
        }

        void closeButtonPressed() override { app.systemRequestedQuit(); }

    private:
        JUCEApplication& app;
    };

    std::unique_ptr<MainWindow> mainWindow;
};

// This macro generates the main() routine that launches the app.
START_JUCE_APPLICATION(Application)
