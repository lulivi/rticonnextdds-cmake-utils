/*
 * (c) Copyright, Real-Time Innovations, 2024.  All rights reserved.
 * RTI grants Licensee a license to use, modify, compile, and create derivative
 * works of the software solely for use with RTI Connext DDS. Licensee may
 * redistribute copies of the software provided that all such copies are subject
 * to this license. The software is provided "as is", with no warranty of any
 * type, including any warranty for fitness for any purpose. RTI is under no
 * obligation to maintain or support the software. RTI shall not be liable for
 * any incidental or consequential damages arising out of the use or inability
 * to use the software.
 */

/**
 * Apply the submodule patch.
 *
 * @param cmakeUtilsRepoRoot rticonnextdds-cmake-utils repository root directory.
 * @param examplesRepoRoot rticonnextdds-examples repository root directory.
 */
void apply(String cmakeUtilsRepoRoot, String examplesRepoRoot) {
    echo(
        'Applying submodule patch:\n- Dump the contents of the'
        + ' rticonnextdds-cmake-utils repository into its submodule location inside the'
        + ' rticonnextdds-examples repository'
    )
    command.run(
        "cp -r ${cmakeUtilsRepoRoot}/*"
        + " ${examplesRepoRoot}/resources/cmake/rticonnextdds-cmake-utils/"
    )
}

return this
