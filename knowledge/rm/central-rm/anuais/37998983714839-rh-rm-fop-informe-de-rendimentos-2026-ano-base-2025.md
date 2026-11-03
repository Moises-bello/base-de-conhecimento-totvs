---
article_id: 37998983714839
category: Anuais
content_hash: 0d347a8dc26df57250632fd4112345207ff2ddfbca13dd9361db3c77641e920c
fetched_at: '2026-06-28T22:46:50.995030+00:00'
product: rm
section_id: 1500000861142
source: central-rm
title: RH - RM - FOP -Informe de Rendimentos 2026 (Ano-Base 2025)
type: support-article
updated_at: '2026-06-17T18:36:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37998983714839-RH-RM-FOP-Informe-de-Rendimentos-2026-Ano-Base-2025
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37998983698967) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como gerar o informe de rendimento a partir do ano calendário 2025?

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento -  12.1.2502, 12.1.2506, 12.1.2510

**Solução**

##### **Qual é o pré-requisito para gerar o Informe de Rendimentos 2026 (Ano-Base 2025)?**

Para que o informe seja gerado, é obrigatório marcar os parâmetros:

* + Deletar Ano de Referência
  + Atualizar dados Informe de Rendimentos – RM Portal

##### **O produto sofrerá melhorias para o Informe de Rendimentos de 2026?**

Sim. Iremos realizar algumas tratativas no menu Anuais | DIRF/Informe de Rendimentos, sendo elas:

1 – Desabilitar alguns parâmetros no Informe de Rendimentos (ano > 2024). Quando o ano informado for superior a 2024, manter desabilitados os parâmetros:

* Usa filtro de seleção ao gerar DIRF em Arquivo
* Utiliza descrição da seção selecionada na DIRF em Arquivo  
  (ambos os paramentos não se aplicam mais após o fim da DIRF)

![](https://tdn.totvs.com/download/attachments/1014658015/image-2026-1-6_13-46-42.png?version=1&modificationDate=1767718002417&api=v2)

2 – Adequar a tabela PDIRF para geração no Portal. Como o Informe de Rendimentos do Portal depende da tabela PDIRF, será necessário habilitar os parâmetros:

* Deletar Ano de Referência
* Atualizar dados Informe de Rendimentos – RM Portal

##### **É necessária a atualização de algum patch?**

No momento não, pois não haverá alterações na geração do Informe de Rendimentos por parte do produto. As mudanças previstas referem-se apenas à usabilidade de telas conforme mencionado no item 02 acima.   
Dessa forma, não é obrigatória a atualização do patch para a geração do Informe de Rendimentos.

No entanto, caso o governo publique alguma alteração que exija adequações no produto, os ajustes necessários serão realizados e disponibilizados nasreleases de mercado 12.1.2502, 12.1.2506, 12.1.2510 e posteriores.

##### **Qual o prazo de entrega do Informe de Rendimentos?**

O prazo é 27 de fevereiro de 2026.

##### **Passo a passo para geração do Informe de Rendimentos?**

* Geração do Informe de Rendimentos através do menu Anuais | DIRF/Informe de Rendimentos.
* A conferência poderá ser realizada de duas formas:
  + Relatório de conferência de IRRF (Painel de Conferência de IRRF)
    - [Middleware - Relatório de Conferência de IRRF](https://tdn.totvs.com/pages/viewpage.action?pageId=782303914)
    - [TAF - Painel de Conferência de IRRF](https://tdn.totvs.com/pages/viewpage.action?pageId=781873283)
  + [Middleware - Relatório de Conferência IRRF S-5002](https://tdn.totvs.com/pages/viewpage.action?pageId=1028947938)
  + Ficha Financeira.

**ATENÇÃO:** A geração doInforme de Rendimentos utiliza exclusivamente as informações apuradas no **cálculo da Folha de Pagamento**, ou seja, **não busca informações no retorno do evento S-5002**.

##### **Saiba mais:**

* [Fim da DIRF X eSocial](https://www.youtube.com/watch?v=f7hzXfAqMkg)
* [DT - Informe de Rendimentos e DIRF 2026](https://tdn.totvs.com/display/LRM/DT+-+Informe+de+Rendimentos+e+DIRF+2026)
* [Informe de Rendimentos e DIRF 2026](https://tdn.totvs.com/display/public/LRM/Informe+de+Rendimentos+e+DIRF+2026#1-1)
