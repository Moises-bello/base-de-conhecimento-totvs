---
article_id: 31669696693783
category: Funcionários
content_hash: da88127b7564c0ca5943a76fe60ddeb0a253f80b430bcd7e200f915120e301a7
fetched_at: '2026-06-28T22:47:35.764177+00:00'
product: rm
section_id: 6149630524311
source: central-rm
title: 'RH - RM - SMT - Atestado: Comportamento do sistema ao utilizar o Antigo Atestado'
type: support-article
updated_at: '2025-12-15T21:33:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31669696693783-RH-RM-SMT-Atestado-Comportamento-do-sistema-ao-utilizar-o-Antigo-Atestado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31669678723991) Tempo aproximado para leitura: **00:05:00 min****Dúvida**Qual o comportamento do sistema quando utiliza-se o Antigo Atestado em relação a situação do funcionário?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Segurança e Saúde Ocupacional – A partir da versão 12.1.24  
  
  
**Solução**Quando o sistema está parametrizado para a utilização do modelo 'Antigo' do Atestado, ou seja, quando ao acessar o módulo **Segurança e Saúde Ocupacional** | **Opções** | **Parametrizador** | **Validações** e o parâmetro referente ao **Novo Atestado estiver desmarcado**, algumas regras serão aplicadas ao atestado que estão associados a **afastamentos.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/31669745404311)**

**1 - Datas de Início e Fim do Atestado em competência anterior a atual competência do Labore**:  
- Sistema não altera a situação do Funcionário  
- Históricos de Afastamento e Situação são preenchidos com as datas de início e fim do atestado.  
  
**2 - Data de Início do Atestado em competência anterior e Fim na atual competência do Labore**:  
- Sistema apresenta uma mensagem ao usuário com as opções (exemplo):  
     *O funcionário está passando da situação "Ativo" para "Af.Previdência"!*  
*Deseja manter o funcionário na situação anterior ao lançamento desse atestado?*  
*- SIM: O funcionário ficará com a situação "Ativo".*  
*- NÃO: O funcionário ficará com a situação "Af.Previdência".*  
  
***Escolhendo a opção SIM:***

- Sistema não altera a situação do Funcionário

- Históricos de Afastamento e Situação são preenchidos com as datas de início e fim do Atestado.

***Escolhendo a opção NÃO*:**

- Sistema altera a situação do Funcionário para a Situação de Afastamento definida no Atestado.  
- Histórico de Situação é preenchido apenas com a Data Início do Atestado.  
- Histórico de Afastamento é preenchido com as Datas de Início e Fim.

**3 - Data de Início do Atestado em competência anterior e Fim em competência futura**:  
- Sistema altera a situação do Funcionário para a Situação de Afastamento definida no Atestado.  
- Histórico de Situação é preenchido apenas com a Data Início do Atestado.  
- Histórico de Afastamento é preenchido com as Datas de Início e Fim.

**4 - Data de Início do Atestado em competência anterior e Data Fim não informada**:  
- Sistema altera a situação do Funcionário para a Situação de Afastamento definida no Atestado.  
- Históricos de Afastamento e Situação são preenchidos apenas com a Data Início do Atestado.

**5 - Datas de Início e Fim do Atestado na atual competência do Labore**:  
- Sistema apresenta uma mensagem ao usuário com as opções e comportamentos citados no item 2.

**6 - Data de Início do Atestado na atual competência do Labore e Fim em competência futura**:  
- Sistema apresenta uma mensagem ao usuário com as opções e comportamentos citados no item 2.

**7 - Data de Início do Atestado na atual competência do Labore e Data Fim não informada**:

Sistema altera a situação do Funcionário para a Situação de Afastamento definida no Atestado.  
- Históricos de Afastamento e Situação são preenchidos apenas com a Data Início do Atestado.

**8 - Datas de Início e Fim do Atestado em competência futura**:  
- Sistema não altera a situação do Funcionário  
- Históricos de Afastamento e Situação são preenchidos com as Datas de Início e Fim do Atestado.

**9 - Data de Início em competência futura e Data Fim não informada**:  
- Sistema não altera a situação do Funcionário  
- Histórico de Afastamento é preenchido com as Datas de Início do Atestado.  
- Histórico de Situação não é alimentado.

**Foram criadas novas situações para quando uma mensagem perguntando para trocar a situação do Funcionário aparece quando a data fim é inserida em um Atestado que não a possuía.**

**1 - Datas de Início e Fim do Atestado em competência anterior à atual competência do Labore**:

- Sistema altera a situação do Funcionário  
- Históricos de Afastamento e Situação são preenchidos com as datas de início e fim do atestado.  
  
**2 - Data de Início do Atestado em competência anterior e Fim na atual competência do Labore**:  
- Sistema apresenta uma mensagem ao usuário com opções (exemplo):

*O funcionário está passando da situação "Af.Previdência" para "Ativo"!*  
*Deseja manter o funcionário na situação anterior ao lançamento desse atestado?*  
*- SIM: O funcionário ficará com a situação "Ativo".*  
*- NÃO: O funcionário ficará com a situação "Af.Previdência".*  
  
**Escolhendo a opção SIM:**

- Sistema não altera a situação do Funcionário  
- Históricos de Afastamento e Situação são preenchidos com as datas de início e fim do Atestado.

**Escolhendo a opção NÃO:**

- Sistema altera a situação do Funcionário para a Situação Ativo.  
- Histórico de Situação é preenchido apenas com a Data Início.  
- Histórico de Afastamento é preenchido com as Datas de Início e Fim.

**3 - Data de Início do Atestado em competência anterior e Fim em competência futura**:  
- Sistema não altera a situação do Funcionário  
- Histórico de Situação é preenchido apenas com a Data Início do Atestado.  
- Histórico de Afastamento é preenchido com as Datas de Início e Fim.  
  
**4 - Datas de Início e Fim do Atestado na atual competência do Labore**:  
- Sistema apresenta uma mensagem ao usuário com as opções e comportamentos citados no item 2.  
  
**5 - Data de Início do Atestado na atual competência do Labore e Fim em competência futura**:  
- Sistema apresenta uma mensagem ao usuário com as opções e comportamentos citados no item 2.

**6 - Datas de Início e Fim do Atestado em competência futura**:  
- Sistema não altera a situação do Funcionário  
- Históricos de Afastamento e Situação são preenchidos com as Datas de Início e Fim do Atestado.

**Saiba Mais**

Para maiores informações, acesse:

- [Atestados](https://tdn.totvs.com/display/public/LRM/Atestados)

- [RH - RM - SMT - Cadastrar atestado que gera afastamento no TOTVS Folha de Pagamento (RM Labore)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360009848952)

- [RH - RM - SMT - Dúvidas frequentes: Atestados](https://centraldeatendimento.totvs.com/hc/pt-br/articles/23511154711447)
