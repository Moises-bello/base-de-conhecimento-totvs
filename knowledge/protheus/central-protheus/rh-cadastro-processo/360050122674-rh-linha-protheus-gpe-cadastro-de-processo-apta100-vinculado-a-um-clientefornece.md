---
article_id: 360050122674
category: RH - Cadastro Processo
content_hash: baaba440a36d73f66a15ae1231f43c66e776b9c853c53f3237da3ccfe3cb5f11
fetched_at: '2026-06-28T22:44:10.651796+00:00'
product: protheus
section_id: 206971467
source: central-protheus
title: RH - Linha Protheus - GPE - Cadastro de Processo (APTA100) vinculado a um cliente/fornecedor
type: support-article
updated_at: '2026-06-24T19:21:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050122674-RH-Linha-Protheus-GPE-Cadastro-de-Processo-APTA100-vinculado-a-um-cliente-fornecedor
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29414382911255) Tempo aproximado para leitura: 00:01:00 min**

**Dúvida**Rotina cadastro de processos APTA100 vinculado a um cliente/fornecedor .  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) -  Gestão de Pessoal - A partir da versão 12  
  
**Solução**

Esta rotina realiza o **armazenamento** e o **gerenciamento** das principais informações sobre **processos,** a fim de efetuar o **acompanhamento** do seu andamento. Um **processo** pode estar vinculado a um **cliente/fornecedor** da empresa ou pode estar associado somente à **reclamada.**

O **processo** tem início quando a **empresa** recebe uma citação ou notificação do conselho de conciliação prévia. A citação chega pelo Correio, nem sempre como carta registrada e é este o documento base utilizado para instruir o cadastro do novo processo.

Utiliza-se o conceito de **fases** pelas quais passam os **processos,** para facilitar seu **gerenciamento.** As fases servem como um **status** de andamento do processo, sendo que os cadastros do tipo **Audiência, Ocorrência, Sentença** ou **Recurso** atualizam a fase geral do processo sempre pela maior data (campo Data Fase), sendo possível verificar a mudança de fase pela tela de **Recursos.**

As informações dos demais cadastros do sistema estão relacionadas a esta rotina, que é a entidade principal do SIGAAPT, que permite **integração** com o **Gestão de Pessoal** e **Financeiro,** para utilizar os dados do **Cadastro de Funcionários** e gerar os títulos referentes ao processos, no **Financeiro,** quando estes devem ser pagos, respectivamente.

#### **Processos Trabalhistas vinculo com o E-Social**

A inclusão e alteração de registros na **Tabela de Processos Administrativos/Judiciais** do Empregador / Contribuinte / Órgão público, de entidade patronal com representação coletiva de trabalhador, contra um dos órgãos governamentais **envolvidos** no projeto e que tenha influência no cálculo das contribuições, dos **impostos** ou do **FGTS** e de **Outras Empresas****,** quando influenciem no cumprimento das suas obrigações principais e acessórias.

As informações consolidadas desta tabela são utilizadas para validação de outros eventos do e-Social e influenciam na forma e no cálculo dos tributos devidos além do FGTS.

O Empregador / Contribuinte / Órgão público é obrigado a enviar o **Evento S-1070** quando há decisão em processo **administrativo** / **judicial,** que tenha como parte, um dos órgãos partícipes do e-Social e que tenha **influência** na apuração das contribuições, dos **impostos** ou do **FGTS,** bem como no cumprimento de **obrigações trabalhistas** e previdenciárias, e quando houver alteração da decisão durante o andamento do processo.

**Não** devem ser cadastrados neste evento, os processos judiciais em que figurem como parte, o **trabalhador** e o **Empregador / Contribuinte / Órgão público.**

O cadastro do evento **S-1070** é **obrigatório** quando há processo **administrativo** ou quando a decisão do processo judicial for **favorável** ao **contribuinte.**

#### **Campos obrigatórios para o E-Social**

Definição e preenchimento de campos obrigatórios.

**Tipo de Processo** - Tipo de processo, judicial ou administrativo.

**Nº Processo** - Identificação do processo judicial ou administrativo.

**Data****Decisão** - Data de decisão do processo.

**Ind.Suspens.** - Indicativo de suspensão de Exigibilidade.

**Id.Dep.Mont**- Indicativo de Depósito do Montante Integral.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077474333)

#### Cenário exemplo para cadastro de um Processo com vinculo ao E-Social:

![](https://tdn.totvs.com/download/attachments/461921821/image2019-2-28_17-44-41.png?version=1&modificationDate=1551386681377&api=v2)

![](https://tdn.totvs.com/download/attachments/461921821/image2019-2-28_17-45-46.png?version=1&modificationDate=1551386746650&api=v2)

**Saiba Mais**[Artigos sobre Processos Trabalhistas](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206971467-RH-Processos-Trabalhistas)  
Essas documentações também podem ser acessadas através da Carolina, veja como acessar a assistente virtual, via Protheus ou central de atendimento: <https://www.youtube.com/watch?v=T7b4zMlphTI>
