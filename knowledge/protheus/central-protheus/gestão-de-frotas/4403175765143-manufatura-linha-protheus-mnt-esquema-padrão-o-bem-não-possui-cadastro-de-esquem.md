---
article_id: 4403175765143
category: Gestão de Frotas
content_hash: f70d92be8493a17000dd7ae882354ee258ed0f67c02c35971e0197d5adb2e53b
fetched_at: '2026-06-28T22:42:39.417668+00:00'
product: protheus
section_id: 360012117873
source: central-protheus
title: 'Manufatura - Linha Protheus - MNT - Esquema padrão: O bem não possui cadastro
  de esquema padrão de pneus'
type: support-article
updated_at: '2021-06-24T19:06:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403175765143-Manufatura-Linha-Protheus-MNT-Esquema-padr%C3%A3o-O-bem-n%C3%A3o-possui-cadastro-de-esquema-padr%C3%A3o-de-pneus
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:55 min**  
**Ocorrência**No **Gestão de Frotas**, ao tentar incluir um abastecimento de veículo é apresentada a mensagem **Esquema padrão: O bem não possui cadastro de esquema padrão de pneus. É necessário realizar o cadastro previamente para realizar o abastecimento**.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Gestão de Frotas - Versão 12  
  
**Causa**Esse incidente ocorre, pois o parâmetro **MV\_NGABAVL - Validar relacionamento do Veiculo. Informar 1 = Valida, 2 = Nao valida Esquema Pad.; Estrutura Pad.; Manut.Pad.;Manut;** está com a primeira posição igual a **1 - Valida** e a **Família** e o **Tipo modelo** do **Veículo** não possui cadastro na rotina **Esquema padrão - MNTA220**.  
  
**Solução**Para solucionar essa ocorrência:

1. Realize o cadastro do **Esquema padrão** para a **Família** e o **Tipo modelo** do **Veículo**;
2. Ou altere a primeira posição do parâmetro **MV\_NGABAVL** para **2 - Não valida**.
