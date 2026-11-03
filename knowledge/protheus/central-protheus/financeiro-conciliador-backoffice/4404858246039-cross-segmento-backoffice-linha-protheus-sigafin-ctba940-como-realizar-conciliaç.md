---
article_id: 4404858246039
category: Financeiro - Conciliador Backoffice
content_hash: ae70531fe664148497226c5d4665ff6cf1fd133b3eb9a73e4a17006997ad77c4
fetched_at: '2026-06-28T22:37:47.044091+00:00'
product: protheus
section_id: 30769054561431
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - CTBA940- Como realizar
  conciliação automática de baixa em lote
type: support-article
updated_at: '2026-02-27T12:03:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404858246039-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-CTBA940-Como-realizar-concilia%C3%A7%C3%A3o-autom%C3%A1tica-de-baixa-em-lote
---

**Dúvida**  
Como realizar o processo de **CTBA940** **conciliação automática,** quando o banco envia no arquivo de retorno os valores de baixas **CNAB** totalizados por lotes?

**Causa**

**Exemplo:** Foram enviados a banco para pagamento, dois lotes via **CNAB,** no primeiro 10 (Dez) títulos de R$100,00, sendo o total do Lote R$1000,00 e outro com 5 (cinco) títulos de R$1000,00, sendo o total do Lote R$ 5000,00 .

Para o processo de importação do arquivo de conciliação automática **CTBA940**, o banco disponibiliza duas linhas apenas com o total dos lotes, não discriminando os títulos, sendo:

1º linha R$1000,00

2º linha R$5000,00

**Ambiente**  
Cross Segmento - BackOffice Linha Protheus – Financeiro – **CTBA940** - A partir da versão 12.1.17.  
  
**Solução**

No padrão da rotina **CTBA940**, a conciliação automática acontece considerando algumas chaves, inicialmente validando a chave forte.

**Completa - Regra 001 (CR) e Regra 004 (CP)**  
Regra na qual os registros da tabela de origem e destino têm sua chave completa atendida:  
Banco + Agência + Conta + Data do Movimento + Documento + Valor + Carteira

**Mas também existe a conciliação via chaves parciais:**

**Parcial 1 - Regra 002 (CR) e Regra 005 (CP)**  
Regra na qual os registros da tabela de origem e destino têm sua chave parcialmente atendida:  
Banco + Agência + Conta + Documento + Valor + Carteira

**Parcial 2 - Regra 003 (CR) e Regra 006 (CP)**  
Regra na qual os registros da tabela de origem e destino têm sua chave parcialmente atendida:  
Banco + Agência + Conta + Data do Movimento + Valor + Carteira

Ajustado o parâmetro **MV\_BXCNAB = 'S',** será gravado um registro totalizador nas tabelas de movimentações bancáriasdurante a baixa por CNAB ou baixa automática, onde eventualmente pode ser conciliado com base nas chaves.

**Importante**

Para a implantação deste processo, devem ser válidas as particularidades do ambiente.
