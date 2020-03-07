import React from 'react';
import { Link } from 'react-router-dom';
import { Layout, Breadcrumb, Input  } from 'antd';
import './Layout.css';

const { Header, Content, Footer } = Layout;
const { Search } = Input;


const DefaultLayout = (props) => {
    return (
        <Layout className="layout">
        <Header>
        <div>
            <Search
            placeholder="(Currently Inactive)"
            onSearch={value => console.log(props.dataSource)}
            style={{ width: 200 }}
            />
        </div>
        </Header>
        <Content style={{ padding: '0 50px' }}>
            <Breadcrumb style={{ margin: '16px 0' }}>
            <Breadcrumb.Item><Link to="/">Home</Link></Breadcrumb.Item>
            </Breadcrumb>
            <div className="site-layout-content">
                {props.children}
            </div>
        </Content>
        <Footer style={{ textAlign: 'center' }}>Made by Christian Lindeneg</Footer>
        </Layout>
    );
}

export default DefaultLayout;