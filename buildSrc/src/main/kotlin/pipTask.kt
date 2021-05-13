import org.gradle.api.tasks.Exec

open class PipTask : Exec() {

    fun setup(pipFiles: List<String>, pythonPath: String) {
        inputs.files(pipFiles)

        var tempArgs = listOf("install")

        pipFiles.forEach {
                reqFile -> tempArgs += listOf("-r", reqFile.toString())
        }
        setArgs(tempArgs)
        executable = "$pythonPath/pip"
    }
}
