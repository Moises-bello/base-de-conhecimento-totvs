---
content_hash: 8cea4bfdb5c80ce610f65e4131fdb3137d6a6540ae175db31ae022303f99728c
fetched_at: '2026-06-29T00:11:31.951547+00:00'
page_id: '741327400'
product: rm
source: tdn-rm
title: CERC - Parcela
type: documentation
url: https://tdn.totvs.com/display/LRM/CERC+-+Parcela
version: 9
---

Para que o Processo [Integrar Registradora](https://tdn.totvs.com/display/LRM/Empreendimentos+-+Processos+-+Integrar+com+Registradora) seja executado com sucesso quando a Registradora de Recebíveis for a CERC, o TCGI deverá integrar também as **Parcelas** financeiras dos Contratos das vendas..

|  |  |  |  |
| --- | --- | --- | --- |
| **CERC-IM003B - PARCELA** | **CAMPO API - PARCELA** | **CAMPO RM** | **DESCRIÇÃO** |
| Tipo de Operação | tipoOperacao | Ação | O Tipo de Operação a ser realizado na integração dos dados coma  CERC é definido pelo campo de **Ação** da tela do Processo [Integrar Registradora](https://tdn.totvs.com/display/LRM/Empreendimentos+-+Processos+-+Integrar+com+Registradora) |
| Referência Externa - Projeto | referenciaExternaProjeto | Código da Coligada + Empreendimento | É formado com a junção dos campos **[Código da Coligada](https://tdn.totvs.com/display/LRM/Coligada)** (acrescido de zeros à esquerda, para ocupar 4 posições) + **[Empreendimento](https://tdn.totvs.com/pages/viewpage.action?pageId=435105154)** que é o identificador desta entidade (que é preenchido automaticamente pelo TCGI). |
| Referência Externa - Contrato | referenciaExternaContrato | Código da Coligada + Venda/Aluguel | É formado com a junção dos campos **[Código da Coligada](https://tdn.totvs.com/display/LRM/Coligada)**  + **Venda/Aluguel** da aba [Identificação](https://tdn.totvs.com/pages/viewpage.action?pageId=435105242) do Cadastro de Venda. |
| Identificador Único da Parcela na CERC | identificadorUnicoParcelaCerc | Cód. Integração | É o campo **Cód. Integração**, da [Visão das Registradoras das Parcelas](https://tdn.totvs.com/pages/viewpage.action?pageId=740685863), do menu de anexos do cadastro de venda.  Este código de interação é composto pelos campos Código da Coligada, Número da Venda, Grupo (da Parcela), Número da Parcela e Tipo da Parcela |
| Número da Parcela | numeroParcela | Nota Promissória | É o campo **Nota Promissória** da sub aba de Parcelas, da visão do Plano de Financiamento da venda.  Consulte esta [documentação](https://tdn.totvs.com/pages/viewpage.action?pageId=435105113) sobre como para parametrizá-lo |
| Aplicação do Recurso | aplicacaoRecurso | (informação calculada) | É informado com base no campo **Data de Vencimento**, da aba [Identificação](https://tdn.totvs.com/pages/viewpage.action?pageId=445647243) de cada parcela dos [Lançamentos Financeiros](https://tdn.totvs.com/pages/viewpage.action?pageId=435104976), do plano de financiamento da venda, em relação à Data de Entrega da subunidade. |
| Tipo da Série | tipoSerie | Componente | É informado conforme o **[Componente](https://tdn.totvs.com/display/LRM/Plano+-+Componentes)** gerador desta parcela, que é informado no campo de mesmo nome, das [Condições de Financiamento](https://tdn.totvs.com/pages/viewpage.action?pageId=435105209) da venda. |
| Data de Vencimento | dataVencimento | Data de Vencimento | É o campo **Data de Vencimento**, da aba [Identificação](https://tdn.totvs.com/pages/viewpage.action?pageId=445647243) de cada parcela dos [Lançamentos Financeiros](https://tdn.totvs.com/pages/viewpage.action?pageId=435104976), do plano de financiamento da venda |
| Principal | principal | Valor Original | É o campo **Valor Original** da sub aba [Gerais](https://tdn.totvs.com/display/LRM/Aba+Valores), da aba Valores da parcela. |
| Juros | juros | Valor | É o **Valor** atualizado do componente do tipo [juros](https://tdn.totvs.com/display/LRM/Tipos+de+Componentes+-+Juros) da parcela, caso ele exista nas [Condições de Financiamento](https://tdn.totvs.com/pages/viewpage.action?pageId=435105209) desta venda. |
| Correção | correcao | Valor | É o **Valor** atualizado, do componente do tipo [correção monetária](https://tdn.totvs.com/pages/viewpage.action?pageId=435105316) da parcela caso ele exista nas [Condições de Financiamento](https://tdn.totvs.com/pages/viewpage.action?pageId=435105209) desta venda. |
| Valor Presente da Parcela | valorPresenteParcela | Valor Líquido | É o **[Valor Líquido](https://tdn.totvs.com/display/LRM/Aba+Valores)** da parcela, atualizado com o somatório dos valores dos componentes que compõem a mesma. |
| Data da Última Correção | dataUltimaCorrecao | Data Reajuste | É o campo **Data Reajuste**, da sub aba de Parcelas, da visão do Plano de Financiamento da venda.  Caso este campo esteja em branco, ou seja, a venda ainda não foi reajustada, será considerado o campo  **Data Venda/Aluguel** da aba [Identificação](https://tdn.totvs.com/pages/viewpage.action?pageId=435105242) do Cadastro de Venda. |
| Índice de Correção | indiceCorrecao | Moeda/Índice | É realizada uma busca no campo **Moeda/Índice**, dos componentes de atualização monetária, das [Condições de Financiamento](https://tdn.totvs.com/pages/viewpage.action?pageId=435105209) desta parcela. |
| Status da Parcela | statusParcela | Statuslan | É o campo **Statuslan** da Tabela FLAN, que apresenta a situação da parcela.  Se for Baixa Parcial é enviada a situação Em Aberto, pois a CERC não tem este conceito. |
| Data Recebimento | dataRecebimento | Data de Baixa | É o campo **Data de Baixa**, da aba [Identificação](https://tdn.totvs.com/pages/viewpage.action?pageId=445647243) de cada parcela dos [Lançamentos Financeiros](https://tdn.totvs.com/pages/viewpage.action?pageId=435104976), do plano de financiamento da venda |
| Valor Recebido | valorRecebido | Valor Baixado | É o campo **Valor Baixado** da sub aba [Gerais](https://tdn.totvs.com/display/LRM/Aba+Valores), da aba Valores da parcela. |
| Tipo Pagamento | tipoPagamento | (valor fixo) | Atualmente é sempre 1 - Boleto. |
| Multa | multa | Valor | É o **Valor** da Multa de Atraso, que é calculado pelo módulo financeiro no momento da baixa da parcela |
| Mora | mora | Valor | É o Valor dos Juros de Mora, que é calculado pelo módulo financeiro no momento da baixa da parcela |
| Gravame/ Ônus | gravameOnus | Tipo Gravame/Ônus | É o campo **Tipo Gravame/Ônus**, da aba [Integração Registradora Recebíveis](https://tdn.totvs.com/pages/viewpage.action?pageId=737567392), da Subunidade. |
| Data Base da Manutenção | dataBaseManutencao | Data Alteração | É o campo **Data Alteração**, da  [Visão das Registradoras das Parcelas](https://tdn.totvs.com/pages/viewpage.action?pageId=740685863), que é a data de execução do Processo [Integrar Registradora](https://tdn.totvs.com/display/LRM/Empreendimentos+-+Processos+-+Integrar+com+Registradora). |

Após a execução com sucesso do Processo [Integrar Registradora](https://tdn.totvs.com/display/LRM/Empreendimentos+-+Processos+-+Integrar+com+Registradora) o sistema vai abastecer a aba [Visão das Registradoras das Parcelas](https://tdn.totvs.com/pages/viewpage.action?pageId=740685863), do Cadastro de Venda, com as informações relativas à esta integração.
