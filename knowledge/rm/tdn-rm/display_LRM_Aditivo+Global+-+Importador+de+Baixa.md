---
content_hash: 29ebafcf99185e353a02c52cc21ffbac9f792e71ec4f9a7ba0f5cf893b06228f
fetched_at: '2026-06-29T00:10:22.616516+00:00'
page_id: '497919655'
product: rm
source: tdn-rm
title: Aditivo Global - Importador de Baixa
type: documentation
url: https://tdn.totvs.com/display/LRM/Aditivo+Global+-+Importador+de+Baixa
version: 1
---

Registros com  status **“Divergência de Valores”** na visão de auditoria, tem opção de corrigir o valor no Arquivo CSV , corrigir o valor de Tolerância e ou Rodar o processo para gerar um aditivo de alteração global de valores de parcelas com o valor da divergência. O Aditivo utilizará a mesma parametrização dos componentes para ajuste automático na baixa, (componentes a maior e a menor).Mudando o Status para **Pronto para Baixa.**

Habilitar perfil do usuário para utilizar Aditivo Global ( **05.01.04.08** ) Importador – Ajustar Valores Divergentes Via Aditivo Global

Exemplo da utilização do Aditivo Global em Importador fora da Tolerância – Divergência de Valores

Contrato encontra-se sem nenhum Aditivo cadastrado.

Arquivo importado e com Status : Lançamento com Divergência de Valores

Neste exemplo , Tolerância no máximo de R$ 1,00 Real

O valor de Diferença = R$ 2.64 , fora do limite de Tolerância , fazendo o **Status** ficar igual = **Lançamento com Divergência de Valores**

Tentando efetuar a baixa do Título.

Sistema não deixa efeutar Baixa de Títulos com divergências de valores.

Processos | Ajustar Valores Divergentes dos Itens Via Aditivo Global

Executar Processo

Processo executado com sucesso

Status alterado para : Preparado para Baixar

Verificando se no Contrato do Cliente foi criado o Aditivo com esta Diferença.

Aditivo incluído no Contrato do Cliente

Baixando o Arquivo

Processos | Baixar os Itens do Importador

Status = Lançamento Baixado
