---
article_id: 115010343008
category: Gestão de Frotas
content_hash: eac58d0738d52cf725b11c8f6f1e4faf010bb6fc2c096327b1bd2ac3fca17a69
fetched_at: '2026-06-28T22:42:39.523797+00:00'
product: protheus
section_id: 360012117873
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Migração de Base de Dados com Gestão de
  Frotas
type: support-article
updated_at: '2021-08-24T17:21:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115010343008-Manufatura-Linha-Protheus-MNT-Migra%C3%A7%C3%A3o-de-Base-de-Dados-com-Gest%C3%A3o-de-Frotas
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:55 min****Dúvida**Como fazer a migração de base de dados com **Gestão de Frotas**?  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Gestão de Frotas - Todas as versões  
  
**Solução**Para ambientes anteriores a **12.1.33 - Harpia**, quando o módulo de **Manutenção de ativos** é utilizado como **Gestão de Frotas**, ou seja, quando com o parâmetro **MV\_NGMNTFR** **- Indica se a empresa irá utilizar o Gestão de Frota**está igual a **S - Sim**, uma série de alterações é realizada no Sistema. Para ambientes **12.1.33** e posteriores, o **Gestão de Frotas** terá seu próprio módulo com o mesmo nome, módulo **Gestão de Frotas**.  
  
Para possibilitar a correta migração de versão do **Protheus**, seguir os procedimentos a seguir:  
O **SX2.UNQ** é atualizado pela **TOTVS** com base no **SXBRA**, como somente o **Frotas** utiliza o tipo de modelo na chave única, está chave é atualizada via programa nas rotinas de esquema padrão,  
manutenção padrão e outras, não é atualizada no **SX2 - Mapeamento de arquivos** do **SXBRA** atualmente.  
  
Então sugerimos o procedimento abaixo para as tabelas que apresentarem problema de chave única ao executar o programa **CHECKDUPL**:

1. Salvar os dados das tabelas que apresentam problema de chave duplicada.
2. Depois de feito o *backup* das tabelas, *dropar* estas tabelas do banco.
3. Fazer a migração com as tabelas vazias.
4. Depois de terminado a migração entrar no *browse* das rotinas abaixo para atualizar o **X2\_UNICO** das tabelas no **SX2** com tipo de modelo.
   * **Bens Padrão**
   * **Estrutura Padrão**
   * **Manutenção Padrão**
   * **Esquema Padrão**
5. Restaurar os dados das tabelas salvas anteriormente.
6. Fazer homologação do ambiente para verificar se está tudo certo.
