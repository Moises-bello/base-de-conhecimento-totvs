---
article_id: 7380202283799
category: eSocial - Parametrizador
content_hash: c5d53f5aa7613436e415bca0d999d524aa5b254a48d2a2aeea6b24a237dc170f
fetched_at: '2026-06-28T22:47:06.302162+00:00'
product: rm
section_id: 1500000834501
source: central-rm
title: 'RH - RM - FOP - eSocial - Parametrizador eSocial: Integração com TAF'
type: support-article
updated_at: '2024-07-08T11:26:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7380202283799-RH-RM-FOP-eSocial-Parametrizador-eSocial-Integra%C3%A7%C3%A3o-com-TAF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:30 min****Dúvida**Como configurar a etapa **Integração com TAF**do parametrizador eSocial?**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**Para os clientes que utilizam o TAF padrão para integração de eventos do eSocial, é necessário configurar a tela abaixo, presente no menu **Configurações | Parametrizador | eSocial | Integração com TAF**.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7379735212823/mceclip0.png)

Devem ser informados os seguintes dados:

* **Web Service:**  
       **Servidor**: Nome ou IP do Servidor onde o TAF está instalado.  
       **Porta**: Número da porta configurada para conexão.  
       Dados podem ser obtidos na tela de Diagnóstico do TAF (menu **Atualizações | Configs. TAF | Diagnóstico**).
* **Usuário/Senha**: Usuário e senha utilizados para acessar o TAF. Importante ser um usuário com acesso de administrador.
* **Código da Filial TAF**: Código da filial que será considerada no TAF para recebimento das informações transmitidas. Deve ser parametrizado de acordo com o que está preenchido no campo **Cód Filial** presente no cadastro de **Complemento Cadastral** no TAF.
* **Utilizar relacionamento Filial RM x Filial TAF para eventos de funcionário**: Caso o parâmetro seja marcado, cada  evento de funcionário será transmitido para sua filial correspondente no TAF, considerando para isso a parametrização feita na etapa **Filiais (RM x TAF)** desse mesmo parametrizador. Os eventos de tabela serão enviados para a filial que se encontra configurada no campo Código da Filial TAF. **Atenção**: Ao selecionar esse parâmetro, as tabelas de negócio do TAF relacionadas aos Eventos de Tabela do eSocial devem, obrigatoriamente, estar compartilhadas. A realização do compartilhamento de tabelas, por sua vez, só é indicado **no momento da implantação do TAF**.
* **Utilizar filial padrão**: A utilização desse parâmetro fará com que todos os eventos de funcionário que tenham por origem uma filial que não esteja configurada na etapa **Filiais (RM x TAF)**, seja transmitido para uma filial padrão do TAF.
* **Utilizar fila de integração**: Ao marcar esse parâmetro, os eventos enviados para o TAF serão adicionados na **fila de integração** do TAF caso exista algum evento predecessor não integrado.

**Saiba mais**  
Para mais informações, acesse:  
     - [Integração com o TAF](https://tdn.totvs.com/pages/releaseview.action?pageId=452719445)
