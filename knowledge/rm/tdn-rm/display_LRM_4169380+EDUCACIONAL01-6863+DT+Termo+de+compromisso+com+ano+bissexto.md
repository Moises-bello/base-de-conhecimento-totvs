---
content_hash: 8f5b76fdf5cf49c986768555d0de0d3ab5ecb60f49f2afaabc44024a3b14af84
fetched_at: '2026-06-29T00:10:12.355782+00:00'
page_id: '454452670'
product: rm
source: tdn-rm
title: 4169380 EDUCACIONAL01-6863 DT Termo de compromisso com ano bissexto
type: documentation
url: https://tdn.totvs.com/display/LRM/4169380+EDUCACIONAL01-6863+DT+Termo+de+compromisso+com+ano+bissexto
version: 1
---

# ESTÁGIO - TERMO DE COMPROMISSO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Educacional |
| **Função:** | Termo de compromisso |
| **Situação/Requisito:** | Ao gravar o termo de compromisso cuja duração do estágio fosse 2 anos e terminasse após fevereiro de ano bissexto, o sistema apresentava incorretamente erro na validação da duração máxima. |
| **Solução/Implementação:** | Otimização na validação da duração máxima do estágio.  Criado novo parâmetro Educacional | Estágio, campo “Calcular duração máxima em:”. Este campo estará preenchido com valor default “Dia”.  No grupo "Duração máxima de um estágio", marcando o campo “Calcular duração máxima em:”, se utilizar a opção “Dia”, o sistema continuará calculando a duração máxima do estágio contando dias corridos entre a data início e término.  Caso o usuário deseje alterar para “Mês” ou “Ano”, a duração máxima do estágio será calculada observando a quantidade preenchida no campo “Duração”. Ao alterar para “mês” ou “ano”, o sistema emitirá alerta caso ultrapasse 2 anos ou 24 meses. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
| **Pacote:** | N/A |
