---
content_hash: 612e4de15370942d6f4ca261dc2e2fa731b388019486cddbaf86cef830df6212
fetched_at: '2026-06-28T21:35:23.070662+00:00'
page_id: '243649881'
product: fluig
source: tdn-fluig
title: BPM 049 - Por que a notificação de exportação da consulta de solicitações não
  está sendo enviada?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=243649881
version: 7
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** fluig

**Versão:** 1.5.6

# Ocorrência

A exportação da consulta de solicitações não está funcionando no fluig. Recebemos uma mensagem de que o processo está em execução e que serei notificado via e-mail quando finalizar, mas não recebo a notificação.

No log do fluig, encontramos a seguinte mensagem de erro:

 

javatruetrue(SunFontManager.java:376) [rt.jar:1.7.0\_76]
at sun.awt.X11FontManager.(X11FontManager.java:32) [rt.jar:1.7.0\_76]
at sun.reflect.NativeConstructorAccessorImpl.newInstance0(Native Method) [rt.jar:1.7.0\_76]
at sun.reflect.NativeConstructorAccessorImpl.newInstance(NativeConstructorAccessorImpl.java:57) [rt.jar:1.7.0\_76]
at sun.reflect.DelegatingConstructorAccessorImpl.newInstance(DelegatingConstructorAccessorImpl.java:45) [rt.jar:1.7.0\_76]
at java.lang.reflect.Constructor.newInstance(Constructor.java:526) [rt.jar:1.7.0\_76]
at java.lang.Class.newInstance(Class.java:379) [rt.jar:1.7.0\_76]
at sun.font.FontManagerFactory$1.run(FontManagerFactory.java:83) [rt.jar:1.7.0\_76]
at java.security.AccessController.doPrivileged(Native Method) [rt.jar:1.7.0\_76]
at sun.font.FontManagerFactory.getInstance(FontManagerFactory.java:74) [rt.jar:1.7.0\_76]
at java.awt.Font.getFont2D(Font.java:490) [rt.jar:1.7.0\_76]
at java.awt.Font.canDisplayUpTo(Font.java:2059) [rt.jar:1.7.0\_76]
at java.awt.font.TextLayout.singleFont(TextLayout.java:469) [rt.jar:1.7.0\_76]
at java.awt.font.TextLayout.(TextLayout.java:527) [rt.jar:1.7.0\_76]
at org.apache.poi.ss.util.SheetUtil.getColumnWidth(SheetUtil.java:208) [poi-3.10.1.jar:3.10.1]
at org.apache.poi.xssf.streaming.SXSSFSheet.autoSizeColumn(SXSSFSheet.java:1251) [poi-ooxml-3.10.1.jar:3.10.1]
at org.apache.poi.xssf.streaming.SXSSFSheet.autoSizeColumn(SXSSFSheet.java:1233) [poi-ooxml-3.10.1.jar:3.10.1]
at com.datasul.technology.webdesk.search.controller.ProcessSearcherBO.createHeader(ProcessSearcherBO.java:849) [ecm-ejb.jar:]
at com.datasul.technology.webdesk.search.controller.ProcessSearcherBO.exportProcessSearcher(ProcessSearcherBO.java:650) [ecm-ejb.jar:]
at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method) [rt.jar:1.7.0\_76]
at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:57) [rt.jar:1.7.0\_76]
at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43) [rt.jar:1.7.0\_76]
at java.lang.reflect.Method.invoke(Method.java:606) [rt.jar:1.7.0\_76]
at org.jboss.as.ee.component.ManagedReferenceMethodInterceptor.processInvocation(ManagedReferenceMethodInterceptor.java:52) [jboss-as-ee-7.5.3.Final-redhat-2.jar:7.5.3.Final-redhat-2]
at org.jboss.invocation.InterceptorContext.proceed(InterceptorContext.java:288) [jboss-invocation-1.1.2.Final-redhat-1.jar:1.1.2.Final-redhat-1]
at org.jboss.invocation.WeavedInterceptor.processInvocation(WeavedInterceptor.java:53) [jboss-invocation-1.1.2.Final-redhat-1.jar:1.1.2.Final-redhat-1]
at org.jboss.as.ee.component.interceptors.UserInterceptorFactory$1.processInvocation(UserInterceptorFactory.java:63) [jboss-as-ee-7.5.3.Final-redhat-2.jar:7.5.3.Final-redhat-2]
at org.jboss.invocation.InterceptorContext.proceed(InterceptorContext.java:288) [jboss-invocation-1.1.2.Final-redhat-1.jar:1.1.2.Final-redhat-1]
at org.jboss.invocation.InterceptorContext$Invocation.proceed(InterceptorContext.java:374) [jboss-invocation-1.1.2.Final-redhat-1.jar:1.1.2.Final-redhat-1]
at org.jboss.as.weld.ejb.Jsr299BindingsInterceptor.doMethodInterception(Jsr299BindingsInterceptor.java:86) [jboss-as-weld-7.5.3.Final-redhat-2.jar:7.5.3.Final-redhat-2]
at org.jboss.as.weld.ejb.Jsr299BindingsInterceptor.processInvocation(Jsr299BindingsInterceptor.java:97) [jboss-as-weld-7.5.3.Final-redhat-2.jar:7.5.3.Final-redhat-2]
at org.jboss.as.ee.component.interceptors.UserInterceptorFactory$1.processInvocation(UserInterceptorFactory.java:63) [jboss-as-ee-7.5.3.Final-redhat-2.jar:7.5.3.Final-redhat-2]
at org.jboss.invocation.InterceptorContext.proceed(InterceptorContext.java:288) [jboss-invocation-1.1.2.Final-redhat-1.jar:1.1.2.Final-redhat-1]
at org.jboss.invocation.WeavedInterceptor.processInvocation(WeavedInterceptor.java:53) [jboss-invocation-1.1.2.Final-redhat-1.jar:1.1.2.Final-redhat-1]
at org.jboss.as.ee.component.interceptors.UserInterceptorFactory$1.processInvocation(UserInterceptorFactory.java:63) [jboss-as-ee-7.5.3.Final-redhat-2.jar:7.5.3.Final-redhat-2]
at org.jboss.invocation.InterceptorContext.proceed(InterceptorContext.java:288) [jboss-invocation-1.1.2.Final-redhat-1.jar:1.1.2.Final-redhat-1]
at org.jboss.as.ejb3.component.invocationmetrics.ExecutionTimeInterceptor.processInvocation(ExecutionTimeInterceptor.java:43) [jboss-as-ejb3-7.5.3.Final-redhat-2.jar:7.5.3.Final-redhat-2]
at org.jboss.invocation.InterceptorContext.proceed(InterceptorContext.java:288) [jboss-invocation-1.1.2.Final-redhat-1.jar:1.1.2.Final-redhat-1]
at org.jboss.as.jpa.interceptor.SBInvocationInterceptor.processInvocation(SBInvocationInterceptor.java:47) [jboss-as-jpa-7.5.3.Final-redhat-2.jar:7.5.3.Final-redhat-2]
at org.jboss.invocation.InterceptorContext.proceed(InterceptorContext.java:288) [jboss-invocation-1.1.2.Final-redhat-1.jar:1.1.2.Final-redhat-1]
at org.jboss.as.weld.ejb.EjbRequestScopeActivationInterceptor.processInvocation(EjbRequestScopeActivationInterceptor.java:93) [jboss-as-weld-7.5.3.Final-redhat-2.jar:7.5.3.Final-redhat-2]
at org.jboss.invocation.InterceptorContext.proceed(InterceptorContext.java:288) [jboss-invocation-1.1.2.Final-redhat-1.jar:1.1.2.Final-redhat-1]
at org.jboss.invocation.InitialInterceptor.processInvocation(InitialInterceptor.java:21) [jboss-invocation-1.1.2.Final-redhat-1.jar:1.1.2.Final-redhat-1]
at org.jboss.invocation.InterceptorContext.proceed(InterceptorContext.java:288) [jboss-invocation-1.1.2.Final-redhat-1.jar:1.1.2.Final-redhat-1]
at org.jboss.invocation.ChainedInterceptor.processInvocation(ChainedInterceptor.java:61) [jboss-invocation-1.1.2.Final-redhat-1.jar:1.1.2.Final-redhat-1]
at org.jboss.as.ee.component.interceptors.ComponentDispatcherInterceptor.processInvocation(ComponentDispatcherInterceptor.java:53) [jboss-as-ee-7.5.3.Final-redhat-2.jar:7.5.3.Final-redhat-2]
at org.jboss.invocation.InterceptorContext.proceed(InterceptorContext.java:288) [jboss-invocation-1.1.2.Final-redhat-1.jar:1.1.2.Final-redhat-1]
at org.jboss.as.ejb3.component.pool.PooledInstanceInterceptor.processInvocation(PooledInstanceInterceptor.java:51) [jboss-as-ejb3-7.5.3.Final-redhat-2.jar:7.5.3.Final-redhat-2]
at org.jboss.invocation.InterceptorContext.proceed(InterceptorContext.java:288) [jboss-invocation-1.1.2.Final-redhat-1.jar:1.1.2.Final-redhat-1]
at org.jboss.as.ejb3.tx.CMTTxInterceptor.invokeInNoTx(CMTTxInterceptor.java:266) [jboss-as-ejb3-7.5.3.Final-redhat-2.jar:7.5.3.Final-redhat-2]
... 31 more]]>

# Solução

De acordo com o log do fluig destacado acima, podemos verificar que o processo de exportação foi iniciado, no entanto, durante a geração do arquivo ocorreu o erro 'Could not initialize class sun.awt.X11GraphicsEnvironment' e o processo foi abortado.

Para solucionar o problema, será preciso adicionar o parâmetro "-Djava.awt.headless=true" no arquivo standalone.conf:

bash

Caso o fluig esteja em cluster (com vários nós), será necessário alterar o standalone.conf de TODOS os servidores.

Para que as alterações entrem em vigor será preciso reiniciar os serviços.
