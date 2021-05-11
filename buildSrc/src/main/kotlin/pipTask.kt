import org.gradle.api.tasks.Exec

open class PipTask : Exec() {

    fun setPipFiles(pipFiles: List<String>) {
        inputs.files(pipFiles)

        var tempArgs = listOf("install")

        pipFiles.forEach {
                reqFile -> tempArgs += listOf("-r", reqFile.toString())
        }
        setArgs(tempArgs)
        executable = "pip"
    }
}
