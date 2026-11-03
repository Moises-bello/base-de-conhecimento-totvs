---
article_id: 1500000096841
category: RH - 13º salário
content_hash: 629d420f56141468b65146d0b945557b96e96e3380e9248662a955cf332870d0
fetched_at: '2026-06-28T22:44:00.642192+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE - Como gerar memória de calculo para conferência
  de médias e Adicionais da primeira parcela do 13º
type: support-article
updated_at: '2025-08-20T14:14:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000096841-RH-Linha-Protheus-GPE-Como-gerar-mem%C3%B3ria-de-calculo-para-confer%C3%AAncia-de-m%C3%A9dias-e-Adicionais-da-primeira-parcela-do-13%C2%BA
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26721892949527) Tempo aproximado para leitura: **00:05:00 min**

**Dúvida**Como conferir as médias e Adicionais do 13º salário referente a 1ª parcela, através da memória de cálculo?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.23  
  
**Solução**

Siga as orientações abaixo:

* Habilite a opção memória de cálculo: Acesse, Atualizações > Definições de Cálculo > Mnemônicos
* Altere o Mnemônico **P\_LMEMCALC** para **.T.** para que possa ser recriadas as fórmulas com o **Log ativado** (Toda vez que este mnemônico for alterado as fórmulas serão recriadas).

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10122920366487)

*Atenção! O mnemônico **P\_LMEMCALC** deve ser desativado após sua utilização para conferência do cálculo, pois estando habilitado durante o processamento normal das rotinas que geram memória de cálculo, acarretará a **perda de performance** das mesmas.*

* Realize o **cálculo** da **1ª parcela do cálculo do 13º salário** para o funcionário que deseja conferir, assim os logs serão gravados.
* Acesse, **Consulta** > Cálculo > **Por Funcionário**
* Selecione o funcionário desejado no *browse* da rotina
* Acione a opção: Outras Ações > **Consultar Memória de Cálculo**
* Será apresentada uma tela listando os logs gravados para o funcionário selecionado.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000098562)

* Os registros serão listados em ordem cronológica, do mais novo para o mais antigo. No exemplo, selecionamos o **roteiro 131**:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098969874)

* Ao selecionar o registro desejado, **dê duplo clique** ou ***Enter*** para visualizar em detalhe o *log*.
  + Será aberta uma nova janela com detalhes do *log*.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101190533)

* + **A tela é dividida em 3 partes.**
    - **Superior: possui as seguintes informações:**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098969974)

- Matrícula e Nome do Funcionário

- Data de admissão

- Situação do funcionário no momento do cálculo

- Data e hora de geração

- Usuário do sistema que realizou o cálculo

- Período, Nr. Pagamento, Processo e Roteiro do cálculo realizado.

**-** **In****ferior Esquerda:**

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000095221) 

- Lista das fórmulas com log gravado.

- Ao selecionar o registro, o detalhe do log é exibido no painel direito.

**- Inferior Direita:**

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000098642)

- Exibição do log da fórmula selecionada no painel esquerdo.

**Saiba Mais**Acesse o *link* a seguir para mais informações sobre a memória de cálculo: <https://tdn.totvs.com/pages/releaseview.action?pageId=330831446>

[RH - 13º Salário](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597271-RH-13%C2%BA-sal%C3%A1rio?page=1#articles)
