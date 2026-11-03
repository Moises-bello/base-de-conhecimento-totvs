---
content_hash: ac7897653452de0bcf233e3fd4a3edeb645f18f17706602a0ff586909b4b575a
fetched_at: '2026-06-29T00:11:17.027775+00:00'
page_id: '676047538'
product: rm
source: tdn-rm
title: Regras customizadas para Geração XML TISS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=676047538
version: 21
---

* Parâmetros TISS

"Não enviar a tag "**numeroGuiaOperadora"** caso não seja informado o campo Senha na guia utilizada.". Com ele marcado e não tendo informação no campo Senha, na geração do xml, o sistema não enviará o campo **numeroGuiaOperadora**. Caso tenha o campo "**senha**", a tag sempre será enviada.

* o parâmetro ‘Se prestador executante for pessoa jurídica. Utilizar o prestador informado como profissional "Tiss’.

* Envia equipe TAG, apenas quando credenciado direto no arquivo ZERO

* Regra Geral - Numero do Lote Baseado na remessa ou Fatura

* Regra XMLTerceiro - Enviar Tag indicacaoClinica da Guia de Solicitação de Internação

Quando habilitado este parâmetro o sistema deverá considerar a informação contida no campo Indicação Clínica do cabeçalho da guia de Solicitação de Internação e não mais da Guia de Resumo de internação.

* Ao marcar o Código do Mat\Med sem zeros a esquerda o sistema não pode gerar no XML o numero zero a esquerda ex : "<ans:codigoProcedimento>78761</ans:codigoProcedimento>."

* Regra XMLTerceiro Arquivo 5 - Não enviar itens dentro da faixa SADT

Quando habilitado o parâmetro, o sistema não deverá levar no arquivo Honorário individual (arquivo 5), os itens dentro da Faixa SADT com honorários (grupo 15)

* Ao marcar "**Prefixo Sequencial para numeroGuiaPrestador**", o sistema irá gerar 2 dígitos como prefixo, 00 para o arquivo do hospital e para arquivos de terceiros será gerado um sequencial por guia.

* Ao marcar o parâmetro nas condições contratuais "Agrupa Procedimento" os lançamentos de honorários, diárias, taxas, serviços, diagnose e terapia serão agrupados na mesma data na geração do XML da versão 4.00.00 em seguida.
* Para informar o grau de participação do prestador na aba de Diagnose e Terapia no xml da TISS, deve ser configurada, na elaboração de contas, na aba de Diagnose e Terapia, com isso será gerada no xml o grau de participação correspondente.

  Caso a função não seja informada na tela de Diagnose e Terapia, e o parâmetro ativo do campo Grau de Participação do TISS III estiver selecionado com um valor padrão, preencher com tal valor
