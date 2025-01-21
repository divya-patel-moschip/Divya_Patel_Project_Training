is_hifi_core_less_64mb(){
	return_val="false"
	export CORES_LIST_HIFI_CORE_LESS_64MB=("hifi4_ss_spfpu_7" "hifi1s_bt_iot_spfpu_c0" "hifi3z_ss_spfpu_7" "hifi5_sphpfpu_nn_dm128")
	for values in ${!CORES_LIST_HIFI_CORE_LESS_64MB[*]}
	do
		if [ "$1" == "${CORES_LIST_HIFI_CORE_LESS_64MB[$values]}" ]
		then
			return_val="true"
			break
		else
			return_val="false"
		fi
	done
	echo $return_val
}
read -p "Enter the job name:" name
is_hifi_core_less_64mb $name

