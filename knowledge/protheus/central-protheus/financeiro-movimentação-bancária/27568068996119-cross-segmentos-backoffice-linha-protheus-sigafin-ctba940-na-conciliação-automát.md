---
article_id: 27568068996119
category: Financeiro - Movimentação Bancária
content_hash: 1c9ad35dc8e786456dc5e35f05e538526161ecc8417fabbb973b8c997a595d0c
fetched_at: '2026-06-28T22:38:19.465030+00:00'
product: protheus
section_id: 1500001550402
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBA940 - Na Conciliação
  Automática no vínculo dos valores com os CPF/CNPJ em casos de depósitos com valores
  iguais, será realizado de forma correta
type: support-article
updated_at: '2024-11-05T16:50:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27568068996119-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBA940-Na-Concilia%C3%A7%C3%A3o-Autom%C3%A1tica-no-v%C3%ADnculo-dos-valores-com-os-CPF-CNPJ-em-casos-de-dep%C3%B3sitos-com-valores-iguais-ser%C3%A1-realizado-de-forma-correta
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27568074849047) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Em relação à conciliação automática, como o sistema vinculará os valores com os CPF/CNPJ corretos em casos de depósitos com valores iguais? O sistema evitará vincular documentos errados?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) -Financeiro - A partir da versão 12.1.22.10  
  
**Solução**

Os matches são realizados de duas formas, **manual ou automática**.

**Automática:** São **matches** realizados de forma **automática** pelo sistema. Funcionam da seguinte forma:  
Caso os registros encontrados na busca de acordo com os filtros utilizados, enquadrem-se em uma regra de **match** cadastrada na tabela **QLB (QLB\_REGMAT)**. A rotina já realizará o **match**, e caso o usuário aplicar a conciliação, o registro será conciliado.  
  
Na regra de **Conciliação Bancaria Automática** temos as seguintes regras para os **matches automáticos**:

**Completa** - **Regra 001 (CR) e Regra 004 (CP)**  
Regra na qual os registros da tabela de origem e destino tem sua chave completa atendida:  
**Banco + Agência + Conta + Data do Movimento + Documento + Valor + Carteira**

**Parcial 1** - **Regra 002 (CR) e Regra 005 (CP)**  
Regra na qual os registros da tabela de origem e destino tem sua chave parcialmente atendida:  
**Banco + Agência + Conta + Documento + Valor + Carteira**

**Parcial 2** - **Regra 003 (CR) e Regra 006 (CP)**  
Regra na qual os registros da tabela de origem e destino tem sua chave

**Saiba Mais**[Cross Segmento - Backoffice linha Protheus - SIGAFIN - CTBA940- Novo Conciliador Bancário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/22896337613463)  
[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBA940 - How to Novo Conciliador Backoffice Financeiro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/23945644752279)
