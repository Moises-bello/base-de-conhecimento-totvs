---
content_hash: e50a2b00fea5267eede836b24f4274c9801cc67246135b5d39dc521f9e4480ca
fetched_at: '2026-06-29T00:08:16.253303+00:00'
page_id: '244932181'
product: rm
source: tdn-rm
title: ER_SAUHRM02-66_Entrega de resultados de exames integrado com Controle de Documentos
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_SAUHRM02-66_Entrega+de+resultados+de+exames+integrado+com+Controle+de+Documentos
version: 4
---

|  |  |  |  |
| --- | --- | --- | --- |
| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |  |  |  |
| Especificação |  |  |  |
| Produto | GESTÃO HOSPITALAR - RM | Módulo | RM SAUDE |
| Segmento Executor | Saúde |  |  |
| Projeto¹ | SAUHRM02 | IRM¹ | SAUHRM01-36 |
| Requisito¹ | SAUHRM02-66 | SubTarefa¹ | SAUHRM02-146 |
| Chamado² | **TTJMYC** |  |  |
| Release de Entrega Planejada | Não definido | Réplica | Não necessário |
| País | ( X ) Brasil  (  ) Argentina  (  ) México  (  ) Chile  (  ) Paraguai  (  ) Equador   (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. |  |  |
| Outros |  |  |  |

# \_Toc355276661\_Toc355276662Objetivo

Após liberação dos exames, status "L" no modulo de controle e pedidos de exames, o sistema gerará um controle de documentos para estes. O processo possibilitará a gestão da movimentação dos documentos entre setores via sistema, sem a necessidade de controles paralelos(Planilha Excel).

# \_Toc355276664Definição da Regra de Negócio

**RN001** – Após status de liberado status "L" no módulo de controle de pedidos de exames o sistema irá gerar internamente um controle de documentos para o Exame em questão.   
 **RN002** – Após laudos liberados(L) no módulo de controle de pedidos de exames, o cliente irá gerar via módulo de controle de documentos o envio destes para o setor responsável pela entrega dos mesmos ao pacientes.O setor que recebeu os laudos físicos fará o recebimento via sistema também(Ver fluxo do processo).   
 **RN003** – Após entrega do Exame para o paciente o cliente entrará no módulo de controle de documentos Atualizará o controle de Documentos utilizando a opção **"Entrega"**. Neste processo sistema chamara a tela "Dados de Registro de Entrega de Exames"(ver tela 8). Após preenchimento da mesma, o status do exame na tela de controle de pedidos de exames mudará automaticamente para "E" = Entregue.   
 **RN004 –** Após geração de um controle de documentos para um determinado exame, se houver a necessidade de voltar o laudo para status "R" no controle de pedidos de exames e o mesmo já ter sido movimentado, este deverá ser "Estornado" no controle de documentos.   
 Exemplo: Laudo já estava com status "L" e já havia sido transferido para a recepção.A recepção estorna o documento e este retorna para a área de Origem.   
 **RN005** **–** A opção "Estorno" no controle de documentos deverá retornar sempre a um status anterior.  
 Exemplo: Status = "A confirmar" se estornado volta para o status "Em Aberto" e Muda o status do Laudo para "R" = Correção.   
 **RN006 –** Será criado uma chamada do módulo de controle de documentos a partir da tela de controle de pedidos de exames.   
   
   
 **RN007 – Será Criado um parâmetro para criação ou não e controle de Documento.(Ver tela 10).**  
 **Este parâmetro habilitará mais alguns críterios critérios São eles;**  
 **Paciente:**   
 **Interno;**  
 **Externo;**  
 **Ambos.**  
 **Exames:**  
 **Imagem;**  
 **Labotarório;**  
 **Ambos.**

|  |  |  |  |
| --- | --- | --- | --- |
| Rotinas Envolvidas |  |  |  |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** |
| Preenchimento de Resultado | Alteração | Controle de pedidos de Exames/Preenchimento de resultados |
| Controle de Documentos | Alteração | Faturamento/controle de Documentos |

# Escopo Negativo

# \_Toc355276665Protótipo de Tela

|  |  |
| --- | --- |
| \_Toc355276666**Regras da Interface** |  |
|  |  |
| **RI-001** | Tela 1 – Controle de Pedidos de Exames.   No status Tipo "L" o sistema estará preparado para efetuar as transferências de documentos; |
| **RI-002** | Tela 2 – Controle de Documentos   * Filtar pelo status = "Em Aberto" e Pelo tipo de Documento. |
| **RI-003** | Tela 3 – Geração de Malote. Nesta tela a área de Exames fara a seleção dos documentos a serem enviados a recepção.Após seleção a mesma vai concluir a opção clicando em "Gerar Malote".          Tela 4 - Na geração de Malote o usuário da área de exames poderá direcionar o mesmo para uma pessoa ou para um setor. Após ok o sistema mudará o status para "A Confirmar". Este status aparecerá para a área destino. |
| **RI-004** | Tela 5 – No setor que receberá o malote – Filtrar por "A Confirmar" e Tipo de Documento "Entrega de Exames".            Tela 6 – Confirmar o Recebimento Fisico dos Exames via sistema.            Tela 7 – Após "Confirmar" o status mudará para "Confirmado" e estará pronto para ser entregue ao paciente.        Após entrega via controle de Documentos o sistema chamará a tela "Dados de Registro de Entregas de Exames" após preenchimento desta tela o status no controle de pedidos de exames mudará para "E".     Tela 8. |
| **RI-005** | Tela 9 – Se a recepção precisar estornar um documento o mesmo deverá retornar um status anterior.   No exemplo ele retornará para "A confirmar" para o usuário que enviou Anteriormente. |
| **RI-007** | Tela 10 – Implementação dos parâmetros sinalizados na tela abaixo para indicar a geração ou não do controle de documentos. Ainda será permitido a escolha do tipo de atendimento e tipo de exame para esta geração.   Se o parâmetro **Gera controle documentos p/Entrega Exames** estiver marcado, o sistema deverá habilitar os demais parâmetros do contrario estes devem ficar inabilitados para escolha.   * + **Interno;**   + **Externo;**   + **Ambos.**   + **Imagem;**   + **Labotarório;**   + **Ambos.**       \_GoBack |
|  |  |

# \_Toc355276667Fluxo do Processo

# Dicionário de Dados

Não necessário para o desenvolvimento deste requisito.

# Grupo de Perguntas

Não necessário para o desenvolvimento deste requisito.

# **Consulta Padrão**

Não necessário para o desenvolvimento deste requisito.

# Estrutura de Menu

Não necessário para o desenvolvimento deste requisito.
