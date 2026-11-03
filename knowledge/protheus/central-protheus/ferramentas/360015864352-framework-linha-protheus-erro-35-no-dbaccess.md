---
article_id: 360015864352
category: Ferramentas
content_hash: 283cf82cd0456539b9adf1d92c2a5d0d8f79d930a45547ba507ecc76c82d1018
fetched_at: '2026-06-28T22:42:18.027534+00:00'
product: protheus
section_id: 360000075448
source: central-protheus
title: Framework - Linha Protheus - Erro -35 no DBAccess
type: support-article
updated_at: '2024-05-09T11:10:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015864352-Framework-Linha-Protheus-Erro-35-no-DBAccess
---

**Dúvida**Como solucionar o Erro -35 que é apresentado no DBAccess?  
   
 **Ambiente**Protheus – DBAccess - Todas as versões  
   
**Solução**A partir do **DBAccess 20180606 (build 18.1.1.0)**, foi implementada pela equipe de Tecnologia uma melhoria de proteção na função TCLINK, que faz necessário nos **banco de dados ORACLE** e **OCI Windows** configurar a variável de ambiente **TNS\_ADMIN**.  
  
Documentação da melhoria: <http://tdn.totvs.com/pages/viewpage.action?pageId=347450402>  
Mais detalhes para configurar a OCI em ambiente Windows: [Clique Aqui!](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016077371-MP-FRAME-Configurar-Fonte-de-Dados-OCI-Windows-)Para solucionar este problema, realize as seguintes verificações:  
  
1. Verifique se a **ODBC/OCI** foi criada conforme documentação TDN.  
Mais detalhes para criar a fonte ODBC/OCI: <http://tdn.totvs.com/display/tec/DBAccess+-+Como+fazer>2. **Nome do ambiente** correto;  
  
3. Verifique se o **usuário** do banco de dados configurado no DBAccess **tem permissão** na base de dados criada;  
  
4. Verifique se o **usuário** do banco de dados está **expirado** ou está **bloqueado**;  
  
5. Verifique se o **Teste de Conexão** da ODBC/OCI foi realizado com sucesso;  
  
6. Verifique se foi efetuada a **validação de conexão** via DBAccess Monitor.  
 Mais detalhes: [Clique Aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015860792)  
  
7. Verifique se é exibida alguma mensagem no **DBAccess**.
