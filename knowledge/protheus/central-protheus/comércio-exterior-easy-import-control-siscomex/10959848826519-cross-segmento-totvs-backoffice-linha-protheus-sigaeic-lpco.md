---
article_id: 10959848826519
category: Comércio Exterior - Easy Import Control - Siscomex
content_hash: b89fac9cd305324b0e3ef23a90eb5df3117b94362585d327debd5194ff2a2f30
fetched_at: '2026-06-28T22:39:45.356015+00:00'
product: protheus
section_id: 1500001538441
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - LPCO
type: support-article
updated_at: '2023-09-06T12:35:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10959848826519-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-LPCO
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Solicitação de LPCO (Licenças, Permissões, Certificados e Outros)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control*- a partir da versão 12.1.27  
  
**Solução**

No novo processo, o **LPCO** será o módulo responsável por viabilizar o licenciamentos e permissões dos produtos de maneira prévia ou durante a operação de importação.  
Desta forma, a **LPCO** irá concentrar os dados específicos da operação e fará referência a registros do Catálogo de Produtos com as definições dos produtos.

São objetivos da manutenção de **LPCO**:

* Permitir organizar as informações das solicitações de **LPCO** emitidas junto aos órgãos anuentes.
* Definir Órgão anuente x Formulário de cada solicitação.
* Relacionar os campos do formulário que serão preenchidos e quais informações serão dispostas em tais campos.

Permite a inclusão de uma solicitação de **LPCO** e os campos dos formulários que serão preenchidos.

**Restrições:**

           - Os campos de **ID** e Versão já vêm carregados pelo sistema com a próxima sequência de registro, podendo serem alterados desde que não seja informado um **ID+Sequencia** que já exista no sistema.

           - Os formulários dos órgãos anuentes informados na manutenção deverão possuir o modelo carregado em seu cadastro uma vez que é com base neste modelo que o sistema carrega os campos necessários para o preenchimento do formulário indicado.

1. Acessar o Menu **Atualizações\Portal Unico\LPCO**
2. Clicar no botão "+**Incluir**"
3. Selecione a Filial e clique no botão **OK**
4. No campo "**Desc.LPCO**" informar uma descrição da **LPCO**
5. No campo "Org.Anuente", pressionar **F3** e via consulta, selecionar um código válido ( que exista no cadastro de órgão anuentes )
6. No campo "**Formul.LPCO**", pressionar **F3** e via consulta, selecionar um código válido ( que exista nos detalhes do cadastro de órgão anuentes para o órgão informado )

**Obs:** Neste momento, o sistema irá carregar na parte inferior da tela "**Detalhes da LPCO** - Dados do Formuário" os campos a serem informados de acordo com o formulário **LPCO** indicado. Nos casos em que o formulário não possuir um modelo carregado, o sistema irá apresentar mensagem da falha no carregamento do modelo (por inexistência ou por invalidade do modelo) e não permirá a gravação posterior do registro de **LPCO**.

1. Informe os campos do grid inferior nos campos carregados pelo sistema e em seguida clique em Confirmar para finalizar.
2. Clicar no botão "**X**" no canto superior direito para encerrar a subrotina
3. Clicar no botão "**X**" no canto superior direito para encerrar a rotina.

**Importante:**  
A rotina está sujeita a alterações em relação ao modo como serão utilizadas as informações relativas aos campos de formulário do grid de detalhes da **LPCO**.  
  
**Exemplo do procedimento**

**Saiba mais**[Lpco](https://tdn.totvs.com/display/PROT/Lpco+-+EICLP401)   
[Procedimento para Implantação DUIMP](https://tdn.totvs.com/pages/viewpage.action?pageId=657762135)
