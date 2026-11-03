---
article_id: 31967903434903
category: Folha Mensal
content_hash: 7ce5d3b6fa143103f8476af54a3fe6840414d1c650eb1634c2d25f952cc62100
fetched_at: '2026-06-28T22:46:58.116107+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP - Crédito do Trabalhador -  Medida Provisória Nº 1.292, de 12
  de Março de 2025
type: support-article
updated_at: '2025-07-28T16:31:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31967903434903-RH-RM-FOP-Cr%C3%A9dito-do-Trabalhador-Medida-Provis%C3%B3ria-N%C2%BA-1-292-de-12-de-Mar%C3%A7o-de-2025
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31967873267607) Tempo aproximado para leitura: **00:04:36min****Dúvida**Como o sistema irá tratar o Crédito do Trabalhador, nova modalidade de empréstimo consignado disponibilizada através da MP nº 1292?

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - A partir dos patches: 12.1.2406.277, 12.1.2410.229, 12.1.2502.145, 12.1.2506 e superiores

**Solução**Para que o novo modelo de **Crédito do Trabalhador** seja corretamente tratado, será necessário configurar o sistema RM da seguinte forma:

**• Scripts**

1.1. Após atualização do ambiente, será necessário executar os scripts de criação das tabelas e seus respectivos campos do sistema através do **RM.Atualizador.exe**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31967903407639)

1.2. Serão criadas as tabelas abaixo e seu respectivos campos:

* PFEMPRT
* PFDESCEMPRT
* PGRPLANC
* PREMCREDTRAB - Eventos da remuneração para margem consignável do crédito trabalhador
* PFREMCREDTRAB - Eventos da remuneração para margem consignável do crédito trabalhador (Anexo do Funcionário)

**• Códigos de Cálculo**

2. **Criação dos novos Códigos de Cálculo:**No menu**Administração de Pessoal | Eventos**, será necessário criar os eventos utilizando os novos códigos de cálculo listados abaixo. Para que os CC apareçam, é necessário **realizar o recálculo** de pelo menos 1 funcionário;  
[RH - RM - FOP - Como incluir os novos códigos de cálculo do Empréstimo Consignado - Crédito do Trabalhador?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/31958025784471-RH-RM-FOP-Como-incluir-os-novos-c%C3%B3digos-de-c%C3%A1lculo-do-Empr%C3%A9stimo-Consignado-Cr%C3%A9dito-do-Trabalhador)

* [480 - Desconto Empréstimo Crédito do Trabalhador](https://tdn.totvs.com.br/pages/releaseview.action?pageId=937704422)
* [481 - Provisão Empréstimo Crédito do Trabalhador Folha](https://tdn.totvs.com.br/pages/releaseview.action?pageId=938311697)
* [482 - Remuneração Base Empréstimo Crédito do Trabalhador](https://tdn.totvs.com.br/pages/releaseview.action?pageId=938311709)
* [483 - Insuficiência Saldo Empréstimo Crédito Trabalhador](https://tdn.totvs.com.br/pages/releaseview.action?pageId=938311723)
* [484 - Provento Provisão Empréstimo Créd.Trab.Folha](https://tdn.totvs.com.br/pages/releaseview.action?pageId=938311735)
* [485 - Provisão Crédito Do Trabalhador Férias 1º Mês](https://tdn.totvs.com.br/pages/viewpage.action?pageId=944707652)
* [486 - Provisão Crédito Do Trabalhador Férias 2º Mês](https://tdn.totvs.com.br/pages/viewpage.action?pageId=944707666)
* [487 - Provisão Crédito Trab. Férias 1º Mês Envelope](https://tdn.totvs.com.br/pages/viewpage.action?pageId=944707675)
* [488 - Provisão Crédito Trab. Férias 2º Mês Envelope](https://tdn.totvs.com.br/pages/viewpage.action?pageId=944707680)
* [489 - Adiantamento Provisão Emprést.Crédito](https://tdn.totvs.com.br/pages/viewpage.action?pageId=944707701)

**• Parametrizador**

3.No menu **Configurações | Parametrizador | Folha Normal | Crédito Trabalhador**, deverá ser realizada a devida parametrização para o correto funcionamento do processo, conforme orientações descritas na documentação: [Crédito Trabalhador - Parametrizador](https://tdn.totvs.com.br/pages/releaseview.action?pageId=937259572);

**• Importação**

4. No menu **Folha Mensal | Importações | Importação de Empréstimo Consignado FEBRABAN/ Crédito do Trabalhador** deverá ser importado o arquivo fornecido pelo Portal Emprega Brasil, conforme orientações descritas na documentação: [Importação Empréstimos FEBRABAN / Crédito do Trabalhador](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452719677&draft=true);

5. **Importação/Exportação da Tabela de Empréstimo:**

No menu Configurações | Importações | Importação de dados da folha de pagamento, realizamos a adequação dos leiautes para contemplar os novos campos, conforme descrito nas documentações:

* [Layout Para Importação de Empréstimo](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452719350)
* [Layout Para Importação de Histórico de Empréstimo](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452719189)

**• Cadastro do Funcionário**  
6. No menu **Administração de Pessoal | Funcionário | Anexos | Folha de Pagamento | Empréstimos**, os dados serão automaticamente preenchidos após a importação, conforme descrito na documentação: [Empréstimos Funcionários](https://tdn.totvs.com/pages/releaseview.action?pageId=452719572);  
  
7. No menu **Administração de Pessoal | Funcionário | Anexos | Folha de Pagamento | Empréstimos | Aba Desconto do Empréstimo**, os dados serão automaticamente preenchidos após a importação, conforme descrito na documentação: [Empréstimos Funcionários - Descontos de empréstimos](https://tdn.totvs.com/pages/releaseview.action?pageId=937695241);  
  
**• Outros Processos (Provisão, Rescisão, etc)**  
8. Para a realização de provisionamento, rescisão e outros processos do Crédito do Trabalhador, acesse: [Crédito do Trabalhador - Linha RM - Medida Provisória Nº 1.292, de 12 de Março de 2025](https://tdn.totvs.com/pages/releaseview.action?pageId=925361639)  
  
  
**Importante**Para exemplos de utilização do novo empréstimo,**CLIQUE NO LINK:**   
[RH - RM - FOP - Crédito do Trabalhador - Exemplos de Utilização](https://centraldeatendimento.totvs.com/hc/pt-br/articles/31969117356439-RH-RM-FOP-Cr%C3%A9dito-do-Trabalhador-Exemplos-de-Utiliza%C3%A7%C3%A3o)

**Saiba Mais**

* [RH - RM - FOP - Dúvidas frequentes: Crédito do Trabalhador](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33227187529495-RH-RM-FOP-D%C3%BAvidas-frequentes-Cr%C3%A9dito-do-Trabalhador)
* [FAQ - Crédito do Trabalhador](https://tdn.totvs.com/pages/releaseview.action?pageId=946423249)
* [Crédito do Trabalhador - Linha RM - Medida Provisória Nº 1.292, de 12 de Março de 2025](https://tdn.totvs.com/pages/viewpage.action?pageId=925361639)
* [DT - Crédito do Trabalhador - eSocial](https://tdn.totvs.com/pages/releaseview.action?pageId=925346824)
