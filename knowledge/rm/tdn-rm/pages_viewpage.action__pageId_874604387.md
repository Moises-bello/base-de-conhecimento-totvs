---
content_hash: 65642de96087b7df46db9e7f62480670ae00926f18803361ec2bbb3ec58281e6
fetched_at: '2026-06-29T00:11:59.660332+00:00'
page_id: '874604387'
product: rm
source: tdn-rm
title: Adesão ao Pagamento Recorrente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=874604387
version: 19
---

---

O usuário habilitará o pagamento recorrente das parcelas dos contratos vinculados ao título selecionado para pagamento.

No sistema habilitar para utilização do TPC, caso tenha dúvidas [clique aqui.](https://tdn.totvs.com/x/jAhOI)

O usuário deverá marcar o parâmetro "15.02 - Tesouraria | Geral 3/4 | Permitir habilitar pagamento automático".

**A partir da versão 12.1.2402** foi criado o parâmetro no cadastro do serviço **"Permitir pagamento recorrente"**, por default todos os serviços estarão marcados para permitir o pagamento por Recorrência, essa opção só estará disponível se o sistema estiver parametrizado para usar TPC e o parâmetro acima estiver marcado.

Habilitar Pagamento Recorrente

Para habilitar o pagamento recorrente, o usuário terá que marcar a opção "Habilitar" durante o processo de pagamento com cartão de crédito (Pagamento com cartões da carteira ou pagamento com outro cartão de crédito)

Após **Habilitar** o usuário terá a opção de determinar quais os serviços deseja marcar para recorrência.

 

Recorrência boleto agrupado

**A partir da versão 12.1.2402**para habilitar pagamento por recorrência em boletos agrupados é necessário habilitar o parâmetro **Permite pagamento recorrente em boletos agrupados**, esse parâmetro está disponível em [Parâmetros -> Educacional ->](https://tdn.totvs.com/display/LRM/Tesouraria)[Integração -> Financeiro](https://tdn.totvs.com/pages/viewpage.action?pageId=425459541)[->](https://tdn.totvs.com/display/LRM/Tesouraria)[Educacional](https://tdn.totvs.com/display/LRM/Tesouraria)[-> Fin - Agrupamento](https://tdn.totvs.com/pages/viewpage.action?pageId=425459541)

Quando o boleto é agrupado com vários serviços e um desse serviço no cadastro o parâmetro **"Permitir pagamento recorrente"**esteja desmarcado, a regra recorrência prevalecerá e ao clicar em "**Seguir para pagamento"** será cadastrado a recorrência para todos os serviços do contrato.

Processo cobrança recorrente cartão de crédito - TOTVS Gestão Financeira

Após a recorrência cadastrada, para os próximos boletos existe um processo no TOTVS Gestão Financeira, que ao agendar para executar (normalmente diariamente) será responsável pelo pagamento, baixa e registro da transação. Para saber mais acesse .

Dados do cartão não serão armazenados na base de dados para maior segurança dos usuários.IMPORTANTE!

## **TABELAS UTILIZADAS**

* FINTEGRACAOCARTAO - Tabela de registro de transações com cartões
* FRECORRENCIACARTAO - Tabela principal de registro de pagamento recorrente
* SRECORRENCIACARTAO - Tabela que armazenará dados educacionais para pagamento recorrente

]]>
