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
            onSearch={value => window.location.replace(`/search/${value}`)}
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
        <Footer style={{ textAlign: 'center' }}>Made by <a href="https://github.com/Lindeneg">Lindeneg</a> as a learning project</Footer>
        </Layout>
    );
}

export default DefaultLayout;