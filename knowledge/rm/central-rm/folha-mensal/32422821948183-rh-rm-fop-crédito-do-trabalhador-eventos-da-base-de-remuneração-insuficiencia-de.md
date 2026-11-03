---
article_id: 32422821948183
category: Folha Mensal
content_hash: 072f7d1ee130f5e393fedeb913c59abe386859a921b6b8420666a01fdf846b17
fetched_at: '2026-06-28T22:46:58.061837+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP - Crédito do Trabalhador - Eventos da base de Remuneração (Insuficiencia
  de saldo)
type: support-article
updated_at: '2026-02-06T21:17:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32422821948183-RH-RM-FOP-Cr%C3%A9dito-do-Trabalhador-Eventos-da-base-de-Remunera%C3%A7%C3%A3o-Insuficiencia-de-saldo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32422854852887) Tempo aproximado para leitura: **00:05:00 min**  
**Dúvida**Qual o comportamento do sistema ao informar ou não informar eventos em Configurações | Parametrizador | Folha Normal | Eventos Crédito Trabalhador?

**Ambiente**

TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - A partir dos patches:

12.1.2406.277

12.1.2410.229

12.1.2502.145

12.1.2506 e superiores

**Solução**

Para o cálculo da Margem Consignável, o sistema inicialmente apura a **Base de Remuneração**, a qual corresponde à soma dos proventos que compõem a base de cálculo, deduzidos os respectivos descontos aplicáveis.

A composição dessa Base de Remuneração pode variar conforme a parametrização definida no caminho **Folha de Pagamento | Configuração | Parametrizador | Folha Mensal | Crédito do Trabalhador**. Em especial, o comportamento do cálculo está diretamente relacionado à configuração do parâmetro **“Eventos do Crédito do Trabalhador devem ser adicionados à base de Contribuição Previdenciária”**, bem como à existência ou não de eventos informados na etapa seguinte, denominada **Eventos do Crédito**.

### Regras aplicadas pelo sistema

De acordo com a combinação entre a marcação do parâmetro e o cadastro de eventos, o sistema adota as seguintes regras:

* **Parâmetro desmarcado e sem eventos informados**  
  São considerados exclusivamente os eventos que possuem incidência de INSS.
* **Parâmetro desmarcado e com eventos informados**  
  São considerados apenas os eventos explicitamente informados no parametrizador.
* **Parâmetro marcado e sem eventos informados**  
  São considerados exclusivamente os eventos que possuem incidência de INSS.
* **Parâmetro marcado e com eventos informados**  
  São considerados os eventos com incidência de INSS, somados aos eventos informados no parametrizador.  
  *Este cenário é o mais recomendado, uma vez que reduz a quantidade de eventos a serem cadastrados manualmente, mantendo a consistência da base de cálculo.*

### Observação importante

É comum ocorrer **Insuficiência de Saldo** quando algum evento deixa de compor a Base de Remuneração. Para identificar esse tipo de situação, é possível consultar o **log de cálculo** e, no **código de cálculo 480**, verificar detalhadamente quais eventos estão sendo considerados na formação da Base de Remuneração, conforme demonstrado no print abaixo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38228559929239)

**Importante:** Os eventos de INSS e IRRF não precisam ser informados, pois já serão considerados automaticamente.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32422854854039)

**Dica:** Caso não deseje que determinado evento seja considerado no cálculo da margem consignável, informe apenas os eventos desejados no parametrizador.

Por exemplo: Se o evento de pensão alimentícia não deve ser incluído, basta parametrizar os demais eventos, excluindo esse da configuração.

**Saiba Mais:**

* [RH - RM - FOP - Dúvidas frequentes: Crédito do Trabalhador](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33227187529495-RH-RM-FOP-D%C3%BAvidas-frequentes-Cr%C3%A9dito-do-Trabalhador)
* [FAQ - Crédito do Trabalhador](https://tdn.totvs.com/pages/releaseview.action?pageId=946423249)
* [Crédito do Trabalhador - Linha RM - Medida Provisória Nº 1.292, de 12 de Março de 2025](https://tdn.totvs.com/pages/viewpage.action?pageId=925361639)
