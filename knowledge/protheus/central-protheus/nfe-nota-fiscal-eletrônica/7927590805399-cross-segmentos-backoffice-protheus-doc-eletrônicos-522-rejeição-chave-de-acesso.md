---
article_id: 7927590805399
category: NFe - Nota Fiscal Eletrônica
content_hash: f359f77698a373e90663023149c4dcc963c551f7f6906c5b28e0a6c710187fa4
fetched_at: '2026-06-28T22:40:01.450290+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 522 Rejeição:
  Chave de Acesso referenciada com UF inválida'
type: support-article
updated_at: '2022-08-03T18:45:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7927590805399--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-522-Rejei%C3%A7%C3%A3o-Chave-de-Acesso-referenciada-com-UF-inv%C3%A1lida
---

**Dúvida**Como solucionar a rejeição abaixo:

522 Rejeição: Chave de Acesso referenciada com UF inválida  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.27

Cross Segmentos - TSS - a partir da versão 12

**Solução**

1. A nota original para que traga de forma correta no XML a **chave** deverá estar gravada de forma correta nas tabelas ***SF3, SFT, SF1 ou SF2 nos campos* F3\_CHVNFE, FT\_CHVNFE, F1\_CHVNFE ou F2\_CHVNFE.**
2. Se a nota for formulário próprio = Sim e tenha sido transmitida pela empresa, na rotina de transmissão de nota ir em ***Outra ações -> Monitor -> faixa ou Monitor -> Consulta NF*** para que seja preenchida a chave nas tabelas corretamente.

![Monitor_-_faixa_-_consulta_NF.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4413537271319/Monitor_-_faixa_-_consulta_NF.gif)

     3. Se a nota de origem for de entrada com ***formulário próprio = Não*** verifique se a chave no campo ***F1\_CHVNFE foi digitada*** de forma correta validando a chave no portal da Sefaz no ambiente Nacional ou de Origem.

     4. Além disso, é necessário que as duas notas estejam no mesmo ambiente, ou seja ***duas notas em produção ou as duas em homologação.***

* ***Saiba mais:***

***Para notas de exportação,***

1. Acesse a rotina **Livros Fiscais** -> **Atualizações** -> **Movimentos** -> **NF manual de Saída** -> **Outras ações** ->**Complementos** -> **Exportação**

![20201117_103818.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360099707813/20201117_103818.gif)

2. Preencher nos complementos de exportação, **Número do Registro de Exportação CDL\_NRREG , Chave de Acesso da NF-e recebida para exportação CDL\_CHVEXP, Quantidade do item realmente exportado CDL\_QTDEXP,**  os três campos são obrigatórios
