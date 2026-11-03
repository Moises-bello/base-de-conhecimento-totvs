---
content_hash: 593cc93ee3d88dd0af3aefdbc3dc4dbc30f9e5bae2d77fd80fa5b845c53b3540
fetched_at: '2026-06-29T00:10:52.398739+00:00'
page_id: '572490550'
product: rm
source: tdn-rm
title: Validações TISS Unimed Juíz de Fora
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=572490550
version: 9
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tela Condições Contratuais**
4. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Apenas atendimentos que possuem como Informações Específicas do Convênio "Unimed JF" (Condições Contratuais com Convênio → Aba Eletrônico III – TISS) passam por essas validações.

As validações são:

* Confere se o CID de internação está preenchido. Caso não esteja preenchido e o atendimento é do Monte Sinai, retorna um erro, se for de outro lugar retorna um aviso. A mensagem é "Falta informar o CID. Informe o CID na página Dados do Atendimento do registro de atendimento deste paciente."
* Para cada Guia, confere se a senha está preenchida. Se não está, retorna um erro com a mensagem "Senha não foi informada para esta parcial no registro deste atendimento."
* Para cada Guia verifica se a Data da guia está preenchida. Senão estiver apresenta a mensagem:  "Existem guias sem data de validade da senha preenchida.', 'No atendimento do paciente, aba Guia/Autorização, localize as guias sem data de validade da senha preenchidas e preenche-as.".
* Valida se existem lançamentos para Honorários e/ou SADT com a mesma hora e data. Caso existe a mensagem é exibida: " Existem lançamentos com data/hora iguais.', 'Conferir as datas e horários de realização dos procedimentos (Honorários e SP/Sadt)."

## **02. EXEMPLO DE UTILIZAÇÃO**

Com CID de internação não preenchido:

Guia sem senha:

## **03. TELA CONDIÇÕES CONTRATUAIS**

## **04. TABELAS UTILIZADAS**

* SZATENDIMENTO
* SZATENDAUTORIZ

]]>
