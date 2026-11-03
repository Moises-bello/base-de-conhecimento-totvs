---
article_id: 5254252291991
category: RH - Folha de Pagamento
content_hash: 1bad69701417b7fd10673a8a2e29712b154a7c0a5371f4282a37eace35fba07f
fetched_at: '2026-06-28T22:44:12.167105+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como calcular a devolução INSS férias na folha
  em casos de falta ou INSS férias calculado a maior
type: support-article
updated_at: '2025-11-26T16:34:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5254252291991-RH-Linha-Protheus-GPE-Como-calcular-a-devolu%C3%A7%C3%A3o-INSS-f%C3%A9rias-na-folha-em-casos-de-falta-ou-INSS-f%C3%A9rias-calculado-a-maior
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26346066814615) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como calcular a devolução INSS férias na folha em casos de falta ou INSS férias calculado a maior?  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Solução**Para utilização desse cálculo, foi disponibilizado o Identificador de Cálculo abaixo, que deve estar vinculado a uma verba que não possui incidência para nenhum tributo:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5253971744919)

Então é necessário cadastrar uma nova verba de provento com o Identificador 1412, conforme abaixo:  
1. Acesse Atualizações >Definições de Cálculo> Verbas (GPEA040);  
2. Clique em Incluir e faça o cadastro de uma nova verba de provento definindo o campo "Tipo do Cod" (RV\_TIPOCOD) com valor **1**, e no campo "Id p/Calculo" (RV\_CODFOL) com valor **1412**.  
  
Tratamentos  
**GPS - Guia da Previdência Social e Título da GPS**Devido a devolução do valor do INSS de Férias que é gerado na Folha de Pagamento, ao emitir a Guia da Previdência Social (GPS), o sistema também irá considerar esse valor que foi devolvido, para que o valor da guia não seja emitido em valor superior ao devido. Então, na geração da GPS o sistema automaticamente fará a dedução do INSS que foi devolvido. A base que sofrerá a dedução é aquela é composta pelos Identificadores:

0064 - INSS

0065 - INSS Férias  
  
**Dissídio Retroativo**Caso seja calculado o Dissídio Retroativo de um mês que houve devolução do INSS, o sistema irá considerar automaticamente essa verba, não há necessidade de nenhuma configuração adicional no Cadastro de Verbas. Isso é necessário para que o valor do INSS que foi devolvido seja considerado pelo sistema ao apurar os valores atualizados de INSS que foram obtidos com o reajuste salarial.

**Observação**: Como se trata de uma verba de devolução ela não deve possuir nenhuma incidência na aba Incidências, exceto se o pagamento da folha ocorrer dentro do mês, porque nesse caso deve ser definida com incidência para Imposto de Renda.  
  
**Importante!**Esse ajuste é válido somente quando o desconto do INSS do mês seguinte é demonstrado no primeiro mês de férias, ou rateado, que são configurações possíveis no parâmetro **MV\_DINSSFM**, com as letras **S** ou **R**, respectivamente.

**Saiba mais**  
[Diferença e Devolucao inss ferias](https://tdn.totvs.com/display/PROT/TWANB2_DT_Diferenca_e_Devolucao_inss_ferias)

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
