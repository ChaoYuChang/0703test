import socket
#from pymavlink import mavutil
import mavlink


# 修改的函数：发送MAVLink指令
def send_mavlink_command(client_socket):
    # 构建MAVLink消息
    msg = mavlink.MAVLink_command_long_message(
        target_system=1,
        target_component=1,
        command=mavlink.MAV_CMD_CUSTOM,  # MAV_CMD_DO_DIGICAM_CONTROL command
        confirmation=0,
        param1=0,
        param2=0,
        param3=0,
        param4=0,
        param5=0,
        param6=1,
        param7=1
    )

    print(msg)

    # 发送MAVLink消息
    mavlink_data = msg.pack(mavlink.MAVLink('',0,1))

    print(mavlink_data)

    client_socket.send(mavlink_data)

def send_mavlink_Zoom_In_command(client_socket):
    # 构建MAVLink消息
    msg = mavlink.MAVLink_command_long_message(
        target_system=1,
        target_component=1,
        command=mavlink.MAV_CMD_CUSTOM_Zoom_In,  # MAV_CMD_CUSTOM_Zoom_in command
        confirmation=0,
        param1=1,
        param2=0,
        param3=0,
        param4=0,
        param5=0,
        param6=1,
        param7=1
    )

    print(msg)

    # 发送MAVLink消息
    mavlink_data = msg.pack(mavlink.MAVLink('',0,1))

    print(mavlink_data)

    client_socket.send(mavlink_data)

def send_mavlink_Zoom_Out_command(client_socket):
    # 构建MAVLink消息
    msg = mavlink.MAVLink_command_long_message(
        target_system=1,
        target_component=1,
        command=mavlink.MAV_CMD_CUSTOM_Zoom_Out,  # MAV_CMD_DO_DIGICAM_CONTROL command
        confirmation=0,
        param1=2,
        param2=0,
        param3=0,
        param4=0,
        param5=0,
        param6=1,
        param7=1
    )

    print(msg)

    # 发送MAVLink消息
    mavlink_data = msg.pack(mavlink.MAVLink('',0,1))

    print(mavlink_data)

    client_socket.send(mavlink_data)

def send_mavlink_Zoom_Reset_command(client_socket):
    # 构建MAVLink消息
    msg = mavlink.MAVLink_command_long_message(
        target_system=1,
        target_component=1,
        command=mavlink.MAV_CMD_CUSTOM_Zoom_Reset,  # MAV_CMD_CUSTOM_Zoom_in command
        confirmation=0,
        param1=3,
        param2=0,
        param3=0,
        param4=0,
        param5=0,
        param6=1,
        param7=1
    )

    print(msg)

    # 发送MAVLink消息
    mavlink_data = msg.pack(mavlink.MAVLink('',0,1))

    print(mavlink_data)

    client_socket.send(mavlink_data)

# 修改的主函数
def main():
    # 设置服务器的IP地址和端口
    server_ip = "192.168.137.2"  # 替换为Jetson的实际IP地址
    port = 12345

    # 创建一个TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # 连接到服务器
        client_socket.connect((server_ip, port))

        while True:
            choice = input("请输入数字（1-8）：")
            if choice == '1':
                send_mavlink_command(client_socket)  # 调用发送MAVLink指令的函数
            elif choice == '2':
                send_mavlink_Zoom_In_command(client_socket)
            elif choice == '3':
                send_mavlink_Zoom_Out_command(client_socket)
            elif choice == '4':
                send_mavlink_Zoom_Reset_command(client_socket)
            elif choice in [ '5', '6', '7', '8']:
                # 其他选项...
                pass
            else:
                print("请输入有效数字（1-8）")

    except KeyboardInterrupt:
        print("程序已结束")
	print("程序已结束2")
    finally:
        # 关闭连接
        client_socket.close()

if __name__ == "__main__":
    main()

#test