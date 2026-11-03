---
article_id: 23007581682199
category: Originação de Grãos (OG)
content_hash: 8eb64706a2e57d6c60e10042c155a3bcd44fd680c29bc5f4e81e7fbf62be8689
fetched_at: '2026-06-28T22:45:43.708180+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Procedimento para Implantação em Venda a Ordem
type: support-article
updated_at: '2025-06-23T20:04:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23007581682199-Agro-Linha-Protheus-AGR-Procedimento-para-Implanta%C3%A7%C3%A3o-em-Venda-a-Ordem
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23007581629975) Tempo aproximado para leitura: **00:04:00 min** **Dúvida**Como realizar **Procedimento para Implantação em Venda a Ordem**?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**

O sistema é atualizado logo após a aplicação do pacote de atualizações *Patch* deste chamado.

1. Aplique o *patch* do chamado e execute uma vez a rotina **UPDDISTR**.
2. Logo após a execução desta rotina é alterado o dicionário de dados da base, conforme especificações abaixo:

**1.** Criação de tabela no arquivo **SX2 – Tabelas**:

|  |  |  |  |
| --- | --- | --- | --- |
| **Chave** | **Nome** | **modo** | **PIMÉ** |
| **N7R** | Rotas de Exportação | C | S |
| **N96** | Tipo de Remessa | C | S |
| **N97** | Tp. Remessa x Modal Pág. Exp. | C | S |

 

**2.** Criação de **Campos** no arquivo **SX3 – Campos:**

* Tabela NJR - Contratos

|  |  |
| --- | --- |
| **Campo** | *NJR\_TIPMER* |
| **Tipo** | C - Caractere |
| **Tamanho** | 1 |
| **Decimal** | 0 |
| **Ordem** | 05 |
| **Formato** | @! |
| **Título** | Tipo Mercado |
| **Descrição** | Tipo de Mercado |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Navegar** | Sim |
| **Validação** | Persistência('12') |
| **Porta Cbox** | 1=Interno; 2=Externo |
| **Massa** | 1 |
| **Ajuda** | Definir o tipo de mercado do contrato: Interno ou Externo |
| **Campo** | NJR\_CODEMB |
| **Tipo** | *C* |
| **Tamanho** | *30* |
| **Decimal** | *0* |
| **Formato** | *@!* |
| **Título** | Embalagem |
| **Descrição** | Código da Embalagem |
| **Nível** | *1* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Navegar** | *Não* |
| **Contras. padrão** | EE5 |
| **Opções** |  |
| **Quando** |  |
| **Relação** |  |
| **Val. Sistema** | vazio() .ou. ExistCPO("EE5") |
| **Massa** | 5 |
| **Ajuda** | *Código da Embalagem.* |

 

|  |  |
| --- | --- |
| **Campo** | *NJR\_DESEMB* |
| **Tipo** | *C* |
| **Tamanho** | *40* |
| **Decimal** | *0* |
| **Formato** | *@!* |
| **Título** | *Desc. Emb.* |
| **Descrição** | Descrição da Embalagem |
| **Nível** | *1* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Navegar** | *Não* |
| **Contras. padrão** |  |
| **Opções** |  |
| **Quando** |  |
| **Inic. Padrão** | IF(!inclui,Posição('EE5',1,xFilial('EE5')+NJR->NJR\_CODEMB,'EE5\_DESC'),' ') |
| **Val. Sistema** |  |
| **Massa** | 5 |
| **Inic. Navegador** | POSIÇÃO('EE5',1,XFILIAL('EE5')+NJR->NJR\_CODEMB,'EE5\_DESC') |
| **Ajuda** | *Descrição da embalagem do produto.* |
| **Campo** | *NJR\_CONDPA* |
| **Tipo** | *C* |
| **Tamanho** | *3* |
| **Decimal** | *0* |
| **Formato** | *@!* |
| **Título** | Mod.Pgto.Exp |
| **Descrição** | Modalidade de Pagamento |
| **Nível** | *1* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Navegar** | *Não* |
| **Contras. padrão** | *AGRAEEF* |
| **Opções** |  |
| **Quando** | *M->NJR\_TIPMER = "2"* |
| **Relação** |  |
| **Val. Sistema** | vazio() .ou. existeCpo("EEF") |
| **Massa** | 6 |
| **Ajuda** | Modalidade de Pagamento do Processo de Exportação. |

 

|  |  |
| --- | --- |
| **Campo** | *NJR\_DESCPA* |
| **Tipo** | *C* |
| **Tamanho** | *50* |
| **Decimal** | *0* |
| **Formato** | *@!* |
| **Título** | Descrição Pago |
| **Descrição** | Descrição Pagamento |
| **Nível** | *1* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Navegar** | *Não* |
| **Contras. padrão** |  |
| **Opções** |  |
| **Quando** |  |
| **Inic. padrão** | IF(!INCLUI,POSICIONE('EEF',1,XFILIAL('EEF')+NJR->NJR\_CONDPA,'EEF\_DESC'),' ') |
| **Val. Sistema** |  |
| **Massa** | 6 |
| **Ajuda** | Descrição da Modalidade de Pagamento de Exportação. |
| **Inic. Navegar** | POSIÇÃO('EEF',1,XFILIAL('EEF')+NJR->NJR\_CONDPA,'EEF\_DESC') |
| **Campo** | *NJR\_VIA* |
| **Tipo** | *C* |
| **Tamanho** | *2* |
| **Decimal** | *0* |
| **Formato** | *@!* |
| **Título** | *Via Transp.* |
| **Descrição** | *Via de Transporte* |
| **Nível** | *1* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Navegar** | *Não* |
| **Contras. padrão** | NJRSYQ |
| **Opções** |  |
| **Quando** | *M->NJR\_TIPMER = "2"* |
| **Relação** |  |
| **Val. Sistema** | vazio() .ou. existeCPO("SYQ") |
| **Massa** | 6 |
| **Ajuda** | Via de Transporte do Contrato para Mercado Externo. |

 

|  |  |
| --- | --- |
| **Campo** | *NJR\_DESVIA* |
| **Tipo** | *C* |
| **Tamanho** | *30* |
| **Decimal** | *0* |
| **Formato** | *@!* |
| **Título** | Descrição Através da |
| **Descrição** | Descrição da Via |
| **Nível** | *1* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Navegar** | *Não* |
| **Contras. padrão** |  |
| **Opções** |  |
| **Quando** |  |
| **Inic. padrão** | IF(!INCLUI,POSICIONE('SYQ',1,XFILIAL('SQY')+NJR->NJR\_VIA,'YQ\_DESCR'),' ') |
| **Val. Sistema** |  |
| **Massa** | 6 |
| **Ajuda** | Descrição da Via de Transporte. |
| **Inic. Navegar** | POSIÇÃO('SYQ',1,XFILIAL('SYQ')+NJR->NJR\_VIA,'YQ\_DESCR') |
| **Campo** | *NJR\_INCOTE* |
| **Tipo** | *C* |
| **Tamanho** | *3* |
| **Decimal** | *0* |
| **Formato** | *@!* |
| **Título** | *Incoterm* |
| **Descrição** | Código INCOTERM |
| **Nível** | *1* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Navegar** | *Não* |
| **Contras. padrão** | *SYJ* |
| **Opções** |  |
| **Quando** | *M->NJR\_TIPMER = "2"* |
| **Relação** | vazio() .ou. existeCPO("SYJ") |
| **Val. Sistema** |  |
| **Massa** | 6 |
| **Ajuda** | Código do INCOTERM. |

 

|  |  |
| --- | --- |
| **Campo** | *NJR\_DESINC* |
| **Tipo** | *C* |
| **Tamanho** | *40* |
| **Decimal** | *0* |
| **Formato** | *@!* |
| **Título** | O INCOTERM |
| **Descrição** | Descrição do INCOTERM |
| **Nível** | *1* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Navegar** | *Não* |
| **Contras. padrão** |  |
| **Opções** |  |
| **Quando** |  |
| **Inic. padrão** | IF(!INCLUI,POSICIONE('SYJ',1,XFILIAL('SYJ')+NJR->NJR\_INCOTE,'YJ\_DESCR'),' ') |
| **Val. Sistema** |  |
| **Massa** | 6 |
| **Ajuda** | Descrição do INCOTERM. |
| **Inic. Navegar** | POSIÇÃO('SYJ',1,XFILIAL('SYJ')+NJR->NJR\_INCOTE,'YJ\_DESCR') |
| **Campo** | *NJR\_CLASSQ* |
| **Tipo** | *C* |
| **Tamanho** | *1* |
| **Decimal** | *0* |
| **Formato** | *@!* |
| **Título** | Contr. Qualificação |
| **Descrição** | Controle de Qualidade |
| **Nível** | *1* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Navegar** | *Não* |
| **Contras. padrão** |  |
| **Opções** | 1=Origem;2=Destino |
| **Quando** |  |
| **Inic. padrão** | '1' |
| **Val. Sistema** | Persistência('12') |
| **Massa** | 6 |
| **Ajuda** | Indica se o controle de qualidade do contrato será na Origem ou no Destino.  (1=Origem;2=Destino) |
| **Inic. Navegar** |  |

 

|  |  |
| --- | --- |
| **Campo** | *NJR\_TPSEVO* |
| **Tipo** | *C* |
| **Tamanho** | *1* |
| **Decimal** | *0* |
| **Formato** | *@!* |
| **Título** | Volume Sel Tp |
| **Descrição** | Tipo Seleção de Volumes |
| **Nível** | *1* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Navegar** | *Não* |
| **Contras. padrão** |  |
| **Opções** | 1=Por Volume;2=Por Bloco;3=Por Fardo |
| **Quando** |  |
| **Inic. padrão** | IIF((M->NJR\_INCOTE == 'CIF' .OR. M->NJR\_INCOTE == 'CFR'),'1','2') |
| **Val. Sistema** | Persistência('123') |
| **Massa** |  |
| **Ajuda** | Indica como selecionar Volumes na Instrução de Embarque, podendo ser:  1-Por Volume;  2-Por Blocos  3-Por Fardos |
| **Inic. Navegar** |  |
| **Campo** | *NJR\_CONDPG* |
| **Tipo** | *C* |
| **Tamanho** | *5* |
| **Decimal** | *0* |
| **Formato** | *@!* |
| **Título** | *Cond. Pago* |
| **Descrição** | *Cond. Pago* |
| **Nível** | *1* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Navegar** | *Não* |
| **Contras. padrão** | SY6NJR |
| **Opções** |  |
| **Quando** | *M->NJR\_TIPMER = "2"* |
| **Relação** |  |
| **Val. Sistema** |  |
| **Massa** | 6 |
| **Ajuda** | Código da condição de pagamento do contrato. |

 

 

|  |  |
| --- | --- |
| **Campo** | *NJR\_DIASPG* |
| **Tipo** | *N* |
| **Tamanho** | *3* |
| **Decimal** | *0* |
| **Formato** | *999* |
| **Título** | *Dias Pagto* |
| **Descrição** | *Dias Pagamento* |
| **Nível** | *1* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Navegar** | *Sim* |
| **Contras. padrão** | SY6NJR |
| **Opções** |  |
| **Quando** | *M->NJR\_TIPMER = "2"* |
| **Relação** |  |
| **Val. Sistema** |  |
| **Massa** | 6 |
| **Ajuda** | Dias do pagamento |
| **Campo** | *NJR\_DESPG* |
| **Tipo** | *C* |
| **Tamanho** | *50* |
| **Decimal** | *0* |
| **Formato** | *@!* |
| **Título** | Des Cond Pag. |
| **Descrição** | Descrição Cond Pagto |
| **Nível** | *1* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Navegar** | *Não* |
| **Contras. padrão** |  |
| **Opções** |  |
| **Quando** |  |
| **Inic. padrão** |  |
| **Val. Sistema** |  |
| **Massa** | 6 |
| **Ajuda** | Descrição da condição de pagamento |
| **Inic. Navegar** |  |

 

|  |  |
| --- | --- |
| **Campo** | *NJR\_TIPOCL* |
| **Tipo** | *C* |
| **Tamanho** | *1* |
| **Decimal** | *0* |
| **Formato** | *@!* |
| **Título** | *Tipo Cliente* |
| **Descrição** | *Tipo de cliente* |
| **Nível** | *1* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Navegar** | *Sim* |
| **Contras. padrão** |  |
| **Opções** | F=Cons.Final;L=Prod.Rural;R=Revendedor;S=Solidário;X=Exportação/Importação |
| **Quando** |  |
| **Relação** |  |
| **Val. Sistema** | pertence("FLRSX") |
| **Massa** | 1 |
| **Ajuda** | Código do tipo de cliente  F=Cons.Final  L=Produtor Rural  R=Revendedor  S = Solidário  X=Exportação/Importação |

* Tabela N7R - Rotas de Exportação

|  |  |
| --- | --- |
| **Campo** | *N7R\_FILIAL* |
| **Tipo** | *C* |
| **Tamanho** | *2* |
| **Decimal** | *0* |
| **Formato** | *@!* |
| **Título** | *Filial* |
| **Descrição** | *Filial do Sistema* |
| **Nível** | *1* |
| **Usado** | *Sim* |
| **Obrigatório** | *Sim* |
| **Navegar** | *Não* |
| **Contras. padrão** |  |
| **Opções** |  |
| **Quando** |  |
| **Relação** |  |
| **Val. Sistema** |  |
| **Ajuda** | *Filial do sistema.* |
| **Campo** | *N7R\_CODCTR* |
| **Tipo** | *C* |
| **Tamanho** | *6* |
| **Decimal** | *0* |
| **Formato** | *@!* |
| **Título** | *Contrato* |
| **Descrição** | *Código do Contrato* |
| **Nível** | *1* |
| **Usado** | *Sim* |
| **Obrigatório** | *Sim* |
| **Navegar** | *Não* |
| **Contras. padrão** | *NJR* |
| **Opções** |  |
| **Quando** |  |
| **Relação** |  |
| **Val. Sistema** | ExisteCPO("NJR") |
| **Ajuda** | *Código do Contrato.* |

 

|  |  |
| --- | --- |
| **Campo** | *N7R\_TIPO* |
| **Tipo** | *C* |
| **Tamanho** | *1* |
| **Decimal** | *0* |
| **Formato** | *@* |
| **Título** | *Tipo* |
| **Descrição** | *Tipo da Rota* |
| **Nível** | *1* |
| **Usado** | *Sim* |
| **Obrigatório** | *Sim* |
| **Navegar** | *Sim* |
| **Contras. padrão** |  |
| **Opções** | *1=Origem;2=Destino* |
| **Quando** | *M->NJR\_TIPMER = "2"* |
| **Relação** | *'1'* |
| **Val. Sistema** | *Persistência('12')* |
| **Ajuda** | Tipo da Rota: 1=Origem;2=Destino |
| **Campo** | *N7R\_CODROT* |
| **Tipo** | *C* |
| **Tamanho** | *5* |
| **Decimal** | *0* |
| **Formato** | *@!* |
| **Título** | Porto/Aeropo |
| **Descrição** | Código do Porto/Aeroporto |
| **Nível** | *1* |
| **Usado** | *Sim* |
| **Obrigatório** | *Sim* |
| **Navegar** | *Sim* |
| **Contras. padrão** | *SI9* |
| **Opções** |  |
| **Quando** | M->NJR\_TIPMER = "2" |
| **Val. Sistema** | ExistCPO("SY9") |
| **Ajuda** | Código do Porto/Aeroporto. |

 

|  |  |
| --- | --- |
| **Campo** | *N7R\_DESROT* |
| **Tipo** | *C* |
| **Tamanho** | *25* |
| **Decimal** | *0* |
| **Formato** | *@!* |
| **Título** | *Desc. Rota* |
| **Descrição** | *Descrição da Rota* |
| **Nível** | *1* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Navegar** | *Sim* |
| **Contras. padrão** |  |
| **Opções** |  |
| **Quando** |  |
| **Val. Sistema** |  |
| **Ajuda** | *Descrição do Porto/Aeroporto.Descrição da Rota.* |
| **Inic. padrão** | IF(!INCLUI,POSICIONE('SY9',1,XFILIAL('SY9')+N7R->N7R\_CODROT,'Y9\_DESCR'),' ') |
| **Inic. Navegar** | POSIÇÃO('SY9',1,XFILIAL('SY9')+N7R->N7R\_CODROT,'Y9\_DESCR') |

* Tabela N96 - Tipo de Remessa

|  |  |
| --- | --- |
| **Campo** | *N96\_FILIAL* |
| **Tipo** | *C* |
| **Tamanho** | *02* |
| **Decimal** | *0* |
| **Formato** | *@!* |
| **Título** | *Filial* |
| **Descrição** | *Filial do Sistema* |
| **Nível** | *1* |
| **Usado** | *Não* |
| **Obrigatório** | *Não* |
| **Navegar** | *Não* |
| **Contras. padrão** | *(X3\_F3)* |
| **Opções** | *(X3\_CBOX)* |
| **Quando** | *(X3\_QUANDO)* |
| **Val. Sistema** | *(X3\_VÁLIDO)* |
| **Ajuda** | *Filial do Sistema* |
| **Inic. padrão** | *(X3\_RELACAO)* |
| **Inic. Navegar** | *(X3\_INIBRW)* |
| **Campo** | *N96\_CODREM* |
| **Tipo** | *C* |
| **Tamanho** | *03* |
| **Decimal** | *0* |
| **Formato** | *@!* |
| **Título** | *Cod.Tp.Rem.* |
| **Descrição** | *Código Tipo Remessa* |
| **Nível** | *1* |
| **Usado** | *Sim* |
| **Obrigatório** | *Sim* |
| **Navegar** | *Sim* |
| **Contras. padrão** | *(X3\_F3)* |
| **Opções** | *(X3\_CBOX)* |
| **Quando** | *(X3\_QUANDO)* |
| **Val. Sistema** | *(X3\_VÁLIDO)* |
| **Ajuda** | *Código do Tipo Remessa* |
| **Inic. padrão** | *(X3\_RELACAO)* |
| **Inic. Navegar** | *(X3\_INIBRW)* |

 

|  |  |
| --- | --- |
| **Campo** | *N96\_DESREM* |
| **Tipo** | *C* |
| **Tamanho** | *30* |
| **Decimal** | *0* |
| **Formato** | *@!* |
| **Título** | *Des.Tp.Rem.* |
| **Descrição** | *Descrição Tipo Remessa* |
| **Nível** | *1* |
| **Usado** | *Sim* |
| **Obrigatório** | *Sim* |
| **Navegar** | *Sim* |
| **Contras. padrão** | *(X3\_F3)* |
| **Opções** | *(X3\_CBOX)* |
| **Quando** | *(X3\_QUANDO)* |
| **Val. Sistema** | *(X3\_VÁLIDO)* |
| **Ajuda** | *Descrição do Tipo Remessa* |
| **Inic. padrão** | *(X3\_RELACAO)* |
| **Inic. Navegar** | *(X3\_INIBRW)* |

* Tabela N97 - Tp. Remessa x Modal Pág. Exp.

|  |  |
| --- | --- |
| **Campo** | *N97\_FILIAL* |
| **Tipo** | *C* |
| **Tamanho** | *02* |
| **Decimal** | *0* |
| **Formato** | *@!* |
| **Título** | *Filial* |
| **Descrição** | *Filial do Sistema* |
| **Nível** | *1* |
| **Usado** | *Não* |
| **Obrigatório** | *Não* |
| **Navegar** | *Não* |
| **Contras. padrão** | *(X3\_F3)* |
| **Opções** | *(X3\_CBOX)* |
| **Quando** | *(X3\_QUANDO)* |
| **Val. Sistema** | *(X3\_VÁLIDO)* |
| **Ajuda** | *Filial do Sistema* |
| **Inic. padrão** | *(X3\_RELACAO)* |
| **Inic. Navegar** | *(X3\_INIBRW)* |
| **Campo** | *N97\_CODREM* |
| **Tipo** | *C* |
| **Tamanho** | *03* |
| **Decimal** | *0* |
| **Formato** | *@!* |
| **Título** | *Cod.Tp.Rem.* |
| **Descrição** | *Código Tipo Remessa* |
| **Nível** | *1* |
| **Usado** | *Sim* |
| **Obrigatório** | *Sim* |
| **Navegar** | *Não* |
| **Contras. padrão** | *(X3\_F3)* |
| **Opções** | *(X3\_CBOX)* |
| **Quando** | *(X3\_QUANDO)* |
| **Val. Sistema** | *(X3\_VÁLIDO)* |
| **Ajuda** | *Código do Tipo da Remessa* |
| **Inic. padrão** | *(X3\_RELACAO)* |
| **Inic. Navegar** | *(X3\_INIBRW)* |

 

|  |  |
| --- | --- |
| **Campo** | *N97\_MODPAG* |
| **Tipo** | *C* |
| **Tamanho** | *03* |
| **Decimal** | *0* |
| **Formato** | *@!* |
| **Título** | *Cod.Mod.Pág.* |
| **Descrição** | *Bacalhau. Mod. Pág. Exp.* |
| **Nível** | *1* |
| **Usado** | *Sim* |
| **Obrigatório** | *Sim* |
| **Navegar** | *Sim* |
| **Contras. padrão** | *ACORDO* |
| **Opções** | *(X3\_CBOX)* |
| **Quando** | *(X3\_QUANDO)* |
| **Val. Sistema** | *ExistCpo("EEF")* |
| **Ajuda** | *Código da Modalidade de Pagamento Exportação.* |
| **Inic. padrão** | *(X3\_RELACAO)* |
| **Inic. Navegar** | *(X3\_INIBRW)* |
| **Campo** | *N97\_DESMOD* |
| **Tipo** | *C* |
| **Tamanho** | *50* |
| **Decimal** | *0* |
| **Formato** | *@!* |
| **Título** | *Desc.Mod.Pág.* |
| **Descrição** | *Desc. Mod. Pág. Exp.* |
| **Nível** | *1* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Navegar** | *Sim* |
| **Contras. padrão** | *(X3\_F3)* |
| **Opções** | *(X3\_CBOX)* |
| **Quando** | *(X3\_QUANDO)* |
| **Val. Sistema** | *(X3\_VÁLIDO)* |
| **Ajuda** | *Descrição da Modalidade de Pagamento Exportação.* |
| **Inic. padrão** | *IF(!INCLUI,POSICIONE('EEF',1,XFILIAL('EEF')+N97->N97\_MODPAG,'EEF\_DESC'),' ')* |
| **Inic. Navegar** | *POSIÇÃO('EEF',1,XFILIAL('EEF')+N97->N97\_MODPAG,'EEF\_DESC')* |

 

* Tabela N9A - Regras Fiscais do Contrato

|  |  |
| --- | --- |
| **Campo** | *N9A\_FILIAL* |
| **Tipo** | *C* |
| **Tamanho** | *02* |
| **Decimal** | *0* |
| **Formato** | *@!* |
| **Título** | *Filial* |
| **Descrição** | *Filial* |
| **Nível** | *1* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Navegar** | *Não* |
| **Contras. padrão** | *(X3\_F3)* |
| **Opções** | *(X3\_CBOX)* |
| **Quando** | *(X3\_QUANDO)* |
| **Val. Sistema** | *(X3\_VÁLIDO)* |
| **Ajuda** | *Não possui* |
| **Inic. padrão** |  |
| **Inic. Navegar** |  |
| **Campo** | *N9A\_CODCTR* |
| **Tipo** | *C* |
| **Tamanho** | *06* |
| **Decimal** | *0* |
| **Formato** | *@!* |
| **Título** | *Contrato* |
| **Descrição** | *Código**do Contrato* |
| **Nível** | *1* |
| **Usado** | *Sim* |
| **Obrigatório** | *Sim* |
| **Navegar** | *Sim* |
| **Contras. padrão** | *(X3\_F3)* |
| **Opções** | *(X3\_CBOX)* |
| **Quando** | *(X3\_QUANDO)* |
| **Val. Sistema** | *ExistCpo('NJR',M->N9A\_CODCTR)* |
| **Ajuda** | Código do Contrato |
| **Inic. padrão** |  |
| **Inic. Navegar** |  |

 

|  |  |
| --- | --- |
| **Campo** | *N9A\_ITEM* |
| **Tipo** | *C* |
| **Tamanho** | *03* |
| **Decimal** | *0* |
| **Formato** | *@!* |
| **Título** | *Identidade Entrega* |
| **Descrição** | *Identidade Entrega* |
| **Nível** | *1* |
| **Usado** | *Sim* |
| **Obrigatório** | *Sim* |
| **Navegar** | *Sim* |
| **Contras. padrão** | *(X3\_F3)* |
| **Opções** | *(X3\_CBOX)* |
| **Quando** | *(X3\_QUANDO)* |
| **Val. Sistema** |  |
| **Ajuda** | Identidade Entrega |
| **Inic. padrão** |  |
| **Inic. Navegar** |  |
| **Campo** | *N9A\_SEQPRI* |
| **Tipo** | *C* |
| **Tamanho** | *03* |
| **Decimal** | *0* |
| **Formato** | *@!* |
| **Título** | *Item* |
| **Descrição** | *Sequencial de itens* |
| **Nível** | *1* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Navegar** | *Sim* |
| **Contras. padrão** | *(X3\_F3)* |
| **Opções** | *(X3\_CBOX)* |
| **Quando** | *(X3\_QUANDO)* |
| **Val. Sistema** |  |
| **Ajuda** | Sequencial de itens |
| **Inic. padrão** |  |
| **Inic. Navegar** |  |

 

|  |  |
| --- | --- |
| **Campo** | *N9A\_CODFIN* |
| **Tipo** | *C* |
| **Tamanho** | *06* |
| **Decimal** | *0* |
| **Formato** | *@!* |
| **Título** | *Finalidade* |
| **Descrição** | *Código**da Finalidade* |
| **Nível** | *1* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Navegar** | *Sim* |
| **Contras. padrão** | *(X3\_F3)* |
| **Opções** | *(X3\_CBOX)* |
| **Quando** | *(X3\_QUANDO)* |
| **Val. Sistema** | Vazio() .ou. existeCpo("N8A") |
| **Ajuda** | Deve indicar o código da finalidade |
| **Inic. padrão** |  |
| **Inic. Navegar** |  |
| **Campo** | *N9A\_DESFIN* |
| **Tipo** | *C* |
| **Tamanho** | *40* |
| **Decimal** | *0* |
| **Formato** | *@!* |
| **Título** | *Des. Finalidade* |
| **Descrição** | *Descrição da Finalidade* |
| **Nível** | *1* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Navegar** | *Sim* |
| **Contras. padrão** | *(X3\_F3)* |
| **Opções** | *(X3\_CBOX)* |
| **Quando** | *(X3\_QUANDO)* |
| **Val. Sistema** |  |
| **Ajuda** | Descrição da Finalidade |
| **Inic. padrão** | *Iif(!INCLUI, Posicione('N8A', 1, FwXFilial('N8A') + N9A->N9A\_CODFIN, 'N8A\_DESFIN'), '')* |
| **Inic. Navegar** | Posição('N8A', 1, FwXFilial('N8A') + N9A->N9A\_CODFIN, 'N8A\_DESFIN') |

 

|  |  |
| --- | --- |
| **Campo** | *N9A\_OPEFIS* |
| **Tipo** | *C* |
| **Tamanho** | *25* |
| **Decimal** | *0* |
| **Formato** | *@!* |
| **Título** | *Ópera. Fis.* |
| **Descrição** | *Código**Operação Fiscal* |
| **Nível** | *1* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Navegar** | *Sim* |
| **Contras. padrão** | *(X3\_F3)* |
| **Opções** | *(X3\_CBOX)* |
| **Quando** | *(X3\_QUANDO)* |
| **Val. Sistema** | ExistCpo('SX5','DJ'+M->N9A\_OPEFIS) |
| **Ajuda** | Código da Operação Fiscal |
| **Inic. padrão** |  |
| **Inic. Navegar** |  |
| **Campo** | *N9A\_TES* |
| **Tipo** | *C* |
| **Tamanho** | *03* |
| **Decimal** | *0* |
| **Formato** | *@!* |
| **Título** | *TES* |
| **Descrição** | *Bacalhau. Tes.* |
| **Nível** | *1* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Navegar** | *Sim* |
| **Contras. padrão** | *(X3\_F3)* |
| **Opções** | *(X3\_CBOX)* |
| **Quando** | *(X3\_QUANDO)* |
| **Val. Sistema** | Vazio().Or.ExistCpo('SF4') |
| **Ajuda** | Código do TES |
| **Inic. padrão** |  |
| **Inic. Navegar** |  |

 

|  |  |
| --- | --- |
| **Campo** | *N9A\_TESAUX* |
| **Tipo** | *C* |
| **Tamanho** | *03* |
| **Decimal** | *0* |
| **Formato** | *@!* |
| **Título** | *TES* |
| **Descrição** | *Bacalhau. Tes.* |
| **Nível** | *1* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Navegar** | *Sim* |
| **Contras. padrão** | *(X3\_F3)* |
| **Opções** | *(X3\_CBOX)* |
| **Quando** | *(X3\_QUANDO)* |
| **Val. Sistema** | Vazio().Or.ExistCpo('SF4') |
| **Ajuda** | Código do TES |
| **Inic. padrão** |  |
| **Inic. Navegar** |  |
| **Campo** | *N9A\_CODENT* |
| **Tipo** | *C* |
| **Tamanho** | *06* |
| **Decimal** | *0* |
| **Formato** | *@!* |
| **Título** | *Bacalhau.Ent.Gordura* |
| **Descrição** | *Código**Entidade Faturamen* |
| **Nível** | *1* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Navegar** | *Sim* |
| **Contras. padrão** | *NJ0* |
| **Opções** | *(X3\_CBOX)* |
| **Quando** | *(X3\_QUANDO)* |
| **Val. Sistema** |  |
| **Ajuda** | Código da Entidade |
| **Inic. padrão** |  |
| **Inic. Navegar** |  |

 

|  |  |
| --- | --- |
| **Campo** | *N9A\_LOJENT* |
| **Tipo** | *C* |
| **Tamanho** | *02* |
| **Decimal** | *0* |
| **Formato** | *@!* |
| **Título** | *Loj.Ent.Fat* |
| **Descrição** | *Loja Entidade Faturamento* |
| **Nível** | *1* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Navegar** | *Sim* |
| **Contras. padrão** |  |
| **Opções** | *(X3\_CBOX)* |
| **Quando** | *(X3\_QUANDO)* |
| **Val. Sistema** |  |
| **Ajuda** | Loja da Entidade |
| **Inic. padrão** |  |
| **Inic. Navegar** |  |
| **Campo** | *N9A\_NOMENT* |
| **Tipo** | *C* |
| **Tamanho** | *40* |
| **Decimal** | *0* |
| **Formato** | *@!* |
| **Título** | *Nm.Ent.Gordura* |
| **Descrição** | *Nome Entidade Faturamento* |
| **Nível** | *1* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Navegar** | *Sim* |
| **Contras. padrão** |  |
| **Opções** | *(X3\_CBOX)* |
| **Quando** | *(X3\_QUANDO)* |
| **Val. Sistema** |  |
| **Ajuda** | Nome da Entidade |
| **Inic. padrão** | *IF(!INCLUI,POSICIONE('NJ0',1,XFILIAL('NJ0')+N9A->N9A\_CODENT+N9A->N9A\_LOJENT,'NJ0\_NOME'),' ')* |
| **Inic. Navegar** | POSIÇÃO('NJ0',1,XFILIAL('NJ0')+N9A->N9A\_CODENT+N9A->N9A\_LOJENT,'NJ0\_NOME') |

 

|  |  |
| --- | --- |
| **Campo** | *N9A\_NMLJEN* |
| **Tipo** | *C* |
| **Tamanho** | *20* |
| **Decimal** | *0* |
| **Formato** | *@!* |
| **Título** | *Nm.Lj.Fat* |
| **Descrição** | *Nome Loja Entidade Fatura* |
| **Nível** | *1* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Navegar** | *Sim* |
| **Contras. padrão** |  |
| **Opções** | *(X3\_CBOX)* |
| **Quando** | *(X3\_QUANDO)* |
| **Val. Sistema** |  |
| **Ajuda** | Nome da Loja da Entidade |
| **Inic. padrão** | *IF(!INCLUI,POSICIONE('NJ0',1,XFILIAL('NJ0')+N9A->N9A\_CODENT+N9A->N9A\_LOJENT,'NJ0\_NOMLOJ'),' ')* |
| **Inic. Navegar** | POSIÇÃO('NJ0',1,XFILIAL('NJ0')+N9A->N9A\_CODENT+N9A→N9A\_LOJENT,'NJ0\_NOMLOJ') |
| **Campo** | *N9A\_TIPCLI* |
| **Tipo** | *C* |
| **Tamanho** | *1* |
| **Decimal** | *0* |
| **Formato** | *@!* |
| **Título** | *Tipo Cliente* |
| **Descrição** | *Tipo do Cliente* |
| **Nível** | *1* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Navegar** | *Sim* |
| **Contras. padrão** |  |
| **Opções** | *F=Cons.Final;L=Produtor Rural;R=Revendedor;S=Solidário;X=Exportação* |
| **Quando** | *(X3\_QUANDO)* |
| **Val. Sistema** | Pertence("FLRSX") |
| **Ajuda** | Tipo de Cliente:  Opções Brasil (L,F,R,S,X):  L - Produtor Rural; F - Cons.Final; R - Revendedor; S - ICMS Solidário sem IPI na base; X - Exportação. |
| **Inic. padrão** |  |
| **Inic. Navegar** |  |

 

|  |  |
| --- | --- |
| **Campo** | *N9A\_ENTENT* |
| **Tipo** | *C* |
| **Tamanho** | *6* |
| **Decimal** | *0* |
| **Formato** | *@!* |
| **Título** | *Bacalhau. Ent. Entrada* |
| **Descrição** | *Código Entidade Entrega* |
| **Nível** | *1* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Navegar** | *Sim* |
| **Contras. padrão** | NJ0 |
| **Opções** |  |
| **Quando** | *(X3\_QUANDO)* |
| **Val. Sistema** |  |
| **Ajuda** | Código da Entidade de Entrega |
| **Inic. padrão** | *FwFldGet('NNY\_ENTDES')* |
| **Inic. Navegar** |  |
| **Campo** | *N9A\_LJEENT* |
| **Tipo** | *C* |
| **Tamanho** | *2* |
| **Decimal** | *0* |
| **Formato** | *@!* |
| **Título** | *Loj. Ent. Entrada* |
| **Descrição** | *Loja da entidade Entrega* |
| **Nível** | *1* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Navegar** | *Sim* |
| **Contras. padrão** |  |
| **Opções** |  |
| **Quando** | *(X3\_QUANDO)* |
| **Val. Sistema** |  |
| **Ajuda** | Loja da Entidade Entrega |
| **Inic. padrão** | *FwFldGet('NNY\_LOJDES')* |
| **Inic. Navegar** |  |

 

|  |  |
| --- | --- |
| **Campo** | *N9A\_NMEENT* |
| **Tipo** | *C* |
| **Tamanho** | *40* |
| **Decimal** | *0* |
| **Formato** | *@!* |
| **Título** | *Nm. Ent. Entrada* |
| **Descrição** | *Nome Entidade de Entrega* |
| **Nível** | *1* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Navegar** | *Sim* |
| **Contras. padrão** |  |
| **Opções** |  |
| **Quando** | *(X3\_QUANDO)* |
| **Val. Sistema** |  |
| **Ajuda** | Nome da Entidade de Entrega |
| **Inic. padrão** | *IF(!INCLUI,POSICIONE('NJ0',1,XFILIAL('NJ0')+N9A->N9A\_ENTENT+N9A->N9A\_LJEENT,'NJ0\_NOME'),' ')* |
| **Inic. Navegar** | POSIÇÃO('NJ0',1,XFILIAL('NJ0')+N9A->N9A\_ENTENT +N9A-> N9A\_LJEENT,'NJ0\_NOME') |
| **Campo** | *N9A\_NLJENT* |
| **Tipo** | *C* |
| **Tamanho** | *20* |
| **Decimal** | *0* |
| **Formato** | *@!* |
| **Título** | *Nm. Lj. Entrada* |
| **Descrição** | *Nome Loja Ent. Entrega* |
| **Nível** | *1* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Navegar** | *Sim* |
| **Contras. padrão** |  |
| **Opções** |  |
| **Quando** | *(X3\_QUANDO)* |
| **Val. Sistema** |  |
| **Ajuda** | Nome da Loja de Entidade Entrega |
| **Inic. padrão** | *IF(!INCLUI,POSICIONE('NJ0',1,XFILIAL('NJ0')+N9A->N9A\_ENTENT+N9A-> N9A\_LJEENT,'NJ0\_NOMLOJ'),' ')* |
| **Inic. Navegar** | POSIÇÃO('NJ0',1,XFILIAL('NJ0')+N9A->N9A\_ENTENT+N9A-> N9A\_LJEENT,'NJ0\_NOMLOJ') |

 

|  |  |
| --- | --- |
| **Campo** | *N9A\_OPETRI* |
| **Tipo** | *C* |
| **Tamanho** | *01* |
| **Decimal** | *0* |
| **Formato** | *@!* |
| **Título** | *Op. Triângulo* |
| **Descrição** | *Operação Triangular* |
| **Nível** | *1* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Navegar** | *Sim* |
| **Contras. padrão** |  |
| **Opções** | *1=Sim;2=Não* |
| **Quando** | *(X3\_QUANDO)* |
| **Val. Sistema** | Persistência("12") |
| **Ajuda** | Possui Operação Triangular?  1-Sim; 2-Não |
| **Inic. padrão** | *'2'* |
| **Inic. Navegar** | *'2'* |
| **Campo** | *N9A\_OPEFUT* |
| **Tipo** | *C* |
| **Tamanho** | *01* |
| **Decimal** | *0* |
| **Formato** | *@!* |
| **Título** | *Op. Futuro* |
| **Descrição** | *Operação Venda Futura* |
| **Nível** | *1* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Navegar** | *Sim* |
| **Contras. padrão** |  |
| **Opções** | *1=Sim;2=Não* |
| **Quando** | *(X3\_QUANDO)* |
| **Val. Sistema** | Persistência("12") |
| **Ajuda** | Operação Venda Futura ?  1 - Sim; 2 – Não |
| **Inic. padrão** | *'2'* |
| **Inic. Navegar** | *'2'* |

 

|  |  |
| --- | --- |
| **Campo** | *N9A\_QUANT* |
| **Tipo** | *N* |
| **Tamanho** | *12* |
| **Decimal** | *2* |
| **Formato** | *@E 999.999.999,99* |
| **Título** | *Quantidade* |
| **Descrição** | *Quantidade* |
| **Nível** | *1* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Navegar** | *Sim* |
| **Contras. padrão** |  |
| **Opções** |  |
| **Quando** | *(X3\_QUANDO)* |
| **Val. Sistema** |  |
| **Ajuda** | Quantidade |
| **Inic. padrão** |  |
| **Inic. Navegar** |  |
| **Campo** | *N9A\_QTDINS* |
| **Tipo** | *N* |
| **Tamanho** | *12* |
| **Decimal** | *2* |
| **Formato** | *@E 999.999.999,99* |
| **Título** | *Qt Instruído* |
| **Descrição** | *Quantidade Instruida* |
| **Nível** | *1* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Navegar** | *Sim* |
| **Contras. padrão** |  |
| **Opções** |  |
| **Quando** | *(X3\_QUANDO)* |
| **Val. Sistema** |  |
| **Ajuda** | Quantidade Instruída |
| **Inic. padrão** |  |
| **Inic. Navegar** |  |

 

|  |  |
| --- | --- |
| **Campo** | *N9A\_SDOINS* |
| **Tipo** | *N* |
| **Tamanho** | *12* |
| **Decimal** | *2* |
| **Formato** | *@E 999.999.999,99* |
| **Título** | *Sld. Instru* |
| **Descrição** | *Saldo Instrução* |
| **Nível** | *1* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Navegar** | *Sim* |
| **Contras. padrão** |  |
| **Opções** |  |
| **Quando** | *(X3\_QUANDO)* |
| **Val. Sistema** |  |
| **Ajuda** | Saldo Instrução |
| **Inic. padrão** |  |
| **Inic. Navegar** |  |
| **Campo** | *N9A\_QTDNF* |
| **Tipo** | *N* |
| **Tamanho** | *12* |
| **Decimal** | *2* |
| **Formato** | *@E 999.999.999,99* |
| **Título** | *Qtd. NF* |
| **Descrição** | *Quantidade NF* |
| **Nível** | *1* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Navegar** | *Sim* |
| **Contras. padrão** |  |
| **Opções** |  |
| **Quando** | *(X3\_QUANDO)* |
| **Val. Sistema** |  |
| **Ajuda** | Quantidade NF (faturado/recebido) |
| **Inic. padrão** |  |
| **Inic. Navegar** |  |

 

|  |  |
| --- | --- |
| **Campo** | *N9A\_SDONF* |
| **Tipo** | *N* |
| **Tamanho** | *12* |
| **Decimal** | *2* |
| **Formato** | *@E 999.999.999,99* |
| **Título** | *Sld NF* |
| **Descrição** | *Saldo NF* |
| **Nível** | *1* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Navegar** | *Sim* |
| **Contras. padrão** |  |
| **Opções** |  |
| **Quando** | *(X3\_QUANDO)* |
| **Val. Sistema** |  |
| **Ajuda** | Saldo NF |
| **Inic. padrão** |  |
| **Inic. Navegar** |  |
| **Campo** | *N9A\_FILORG* |
| **Tipo** | *C* |
| **Tamanho** | *02* |
| **Decimal** | *0* |
| **Formato** | *@!* |
| **Título** | *Fil Origem* |
| **Descrição** | *Origem Filial* |
| **Nível** | *1* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Navegar** | *Sim* |
| **Contras. padrão** |  |
| **Opções** |  |
| **Quando** | *(X3\_QUANDO)* |
| **Val. Sistema** | ExistCpo("SM0",cEmpAnt+M->N9A\_FILORG) |
| **Ajuda** | Origem Filial |
| **Inic. padrão** | *FwFldGet('NNY\_FILORG')* |
| **Inic. Navegar** |  |

|  |  |
| --- | --- |
| **Campo** | *N9A\_CODROM* |
| **Tipo** | *C* |
| **Tamanho** | *10* |
| **Decimal** | *0* |
| **Formato** | *@!* |
| **Título** | *Bacalhau Romaneio* |
| **Descrição** | *Código**Romaneio Global* |
| **Nível** | *1* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Navegar** | *Sim* |
| **Contras. padrão** |  |
| **Opções** |  |
| **Quando** | *(X3\_QUANDO)* |
| **Val. Sistema** |  |
| **Ajuda** | Bacalhau Romaneio Global |
| **Inic. padrão** |  |
| **Inic. Navegar** |  |

 

 

|  |  |
| --- | --- |
| **Campo** | *N9A\_PRIORI* |
| **Tipo** | *N* |
| **Tamanho** | *3* |
| **Decimal** | *0* |
| **Formato** | *@E 999* |
| **Título** | *Prioridade* |
| **Descrição** | Prioridade Regra Fiscal |
| **Nível** | *1* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Navegar** | *Sim* |
| **Contras. padrão** |  |
| **Opções** |  |
| **Quando** | *(X3\_QUANDO)* |
| **Val. Sistema** |  |
| **Ajuda** | Prioridade |
| **Inic. padrão** |  |
| **Inic. Navegar** |  |

 

* Tabela NJM - Dados Fiscais do Romaneio

|  |  |
| --- | --- |
| **Campo** | *NJM\_SUBTIP* |
| **Tipo** | *C* |
| **Tamanho** | *2* |
| **Decimal** | *0* |
| **Formato** |  |
| **Título** | *SubTipo Ctrl* |
| **Descrição** | SubTipo de Controle |
| **Nível** | *1* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Navegar** | *Sim* |
| **Contras. padrão** |  |
| **Opções** |  |
| **Quando** |  |
| **Val. Sistema** | ExistCpo('SX5','K0'+M->NJM\_SUBTIP) |
| **Ajuda** | SubTipo de Controle |
| **Inic. padrão** |  |
| **Inic. Navegar** |  |

 

**Importante:**

O tamanho dos campos que possuem grupo pode variar de acordo com o ambiente de uso.

**3.** Criação de **Índices** no arquivo **SIX – Índices**:

|  |  |
| --- | --- |
| **Índice** | *N7R* |
| **Ordem** | *1* |
| **Chave** | *N7R\_FILIAL+N7R\_CODCTR+N7R\_TIPO+N7R\_CODROT* |
| **Descrição** | *Filial+Contrato+Tipo+**Código* |
| **Proprietário** | *S* |
| **Índice** | *N96* |
| **Ordem** | *1* |
| **Chave** | *N96\_FILIAL+N96\_CODREM* |
| **Descrição** | *Filial+Cod.Tp.Rem.* |
| **Proprietário** | *S* |

 

|  |  |
| --- | --- |
| **Índice** | *N97* |
| **Ordem** | *1* |
| **Chave** | *N97\_FILIAL+N97\_CODREM+N97\_MODPAG* |
| **Descrição** | *Filial+Cod.Tp.Rem. + Cod.Mod.Pag.* |
| **Proprietário** | *S* |
| **Índice** | *N97* |
| **Ordem** | *2* |
| **Chave** | *N97\_FILIAL+N97\_MODPAG+N97\_CODREM* |
| **Descrição** | *Filial+Cod.Mod.Pag. + Cod.Tp.Rem.* |
| **Proprietário** | *S* |

 

**4.** Alteração da **Consulta Padrão** no arquivo **SXB – Consulta Padrão**:

* Pesquisa NJRSYQ - Vias Transporte Exp.

|  |  |
| --- | --- |
| **Alias** | *NJRSYQ* |
| **Tipo** | *1* |
| **Sequência** | *01* |
| **Coluna** | BD |
| **Descrição** | Vias Transporte Exp. |
| **Contém** | SYQ |
| **Alias** | *NJRSYQ* |
| **Tipo** | *2* |
| **Sequência** | *01* |
| **Coluna** | 01 |
| **Descrição** | Código |
| **Contém** |  |

 

|  |  |
| --- | --- |
| **Alias** | *NJRSYQ* |
| **Tipo** | *4* |
| **Sequência** | *01* |
| **Coluna** | 01 |
| **Descrição** | Descrição |
| **Contém** | YQ\_DESCR |
| **Alias** | *NJRSYQ* |
| **Tipo** | *4* |
| **Sequência** | *01* |
| **Coluna** | 02 |
| **Descrição** | Código da Via |
| **Contém** | YQ\_VIA |

 

|  |  |
| --- | --- |
| **Alias** | *NJRSYQ* |
| **Tipo** | *5* |
| **Sequência** | *01* |
| **Coluna** |  |
| **Descrição** |  |
| **Contém** | SYQ->YQ\_VIA |

 

* Pesquisa N96 - Tipo de Remessa.

|  |  |
| --- | --- |
| **Alias** | *N96* |
| **Tipo** | *1* |
| **Sequência** | *01* |
| **Coluna** | N96\_CODREM |
| **Descrição** | Tipo de Remessa |
| **Contém** | N96→N96\_CODREM |
| **Alias** | *N96* |
| **Tipo** | *1* |
| **Sequência** | *02* |
| **Coluna** | N96\_CODREM |
| **Descrição** | Tipo de Remessa |
| **Contém** | N96→N96\_DESREM |

 

* Pesquisa AGREEF - Consulta EEF - AGRO.

|  |  |
| --- | --- |
| **Alias** | *N97* |
| **Tipo** | *1* |
| **Sequência** | *01* |
| **Coluna** | EEF\_COD |
| **Descrição** | Código |
| **Contém** | EEF → EEF\_COD |
| **Alias** | *N97* |
| **Tipo** | *1* |
| **Sequência** | *02* |
| **Coluna** | EEF\_DESC |
| **Descrição** | Descrição. |
| **Contém** | EEF → EEF\_DESC |

 

* Pesquisa SY6NJR - Condição de Pagto:

|  |  |
| --- | --- |
| **Alias** | *AJ6* |
| **Tipo** | *1* |
| **Sequência** | *01* |
| **Coluna** | Y6\_COD |
| **Descrição** | Código |
| **Contém** | SY6 → Y6\_COD |
| **Alias** | *AJ6* |
| **Tipo** | *1* |
| **Sequência** | *02* |
| **Coluna** | Y6\_DIAS\_PA |
| **Descrição** | Nº. Dias |
| **Contém** | SY6→ Y6\_DIAS\_PA |

 

**5.** Criação de **Gatilhos** no arquivo **SX7 – Gatilhos**:

Tabela **NJR – Contratos**: 

|  |  |
| --- | --- |
| **Campo** | *NJR\_CODPRO* |
| **Sequência** | *004* |
| **Campo Domínio** | NJR\_CODEMB |
| **Tipo** | *Primário* |
| **Regra** | SB1->B1\_CODEMB |
| **Posição?** | *SIM* |
| **Chave** | xFilial('SB1')+M->NJR\_CODPRO |
| **Condição** |  |
| **Proprietário** |  |
| **Campo** | *NJR\_CODPRO* |
| **Sequência** | *005* |
| **Campo Domínio** | NJR\_DESEMB |
| **Tipo** | *Primário* |
| **Regra** | EE5->EE5\_DESC |
| **Posição?** | *SIM* |
| **Chave** | xFilial('EE5')+M->NJR\_CODEMB |
| **Condição** |  |
| **Proprietário** |  |

 

|  |  |
| --- | --- |
| **Campo** | *NJR\_CODEMB* |
| **Sequência** | *001* |
| **Campo Domínio** | *NJR\_DESEMB* |
| **Tipo** | *Primário* |
| **Regra** | *EE5->EE5\_DESC* |
| **Posição?** | *NÃO* |
| **Chave** | *xFilial('EE5")+M->NJR\_CODEMB* |
| **Condição** |  |
| **Proprietário** |  |
| **Campo** | *NJR\_CONDPA* |
| **Sequência** | *001* |
| **Campo Domínio** | *NJR\_DESCPA* |
| **Tipo** | *Primário* |
| **Regra** | EEF->EEF\_DESC |
| **Posição?** | *NÃO* |
| **Chave** | xFilial('EEF')+M->NJR\_CONDPA |
| **Condição** |  |
| **Proprietário** |  |

 

|  |  |
| --- | --- |
| **Campo** | *NJR\_VIA* |
| **Sequência** | *001* |
| **Campo Domínio** | *NJR\_DESVIA* |
| **Tipo** | *Primário* |
| **Regra** | SYQ->YQ\_DESCR |
| **Posição?** | *NÃO* |
| **Chave** | xFilial('SYQ')+M->NJR\_VIA |
| **Condição** |  |
| **Proprietário** |  |
| **Campo** | *NJR\_INCOTE* |
| **Sequência** | *001* |
| **Campo Domínio** | *NJR\_DESINC* |
| **Tipo** | *Primário* |
| **Regra** | SYJ->YJ\_DESCR |
| **Posição?** | *NÃO* |
| **Chave** | xFilial('SYJ')+M->NJR\_INCOTE |
| **Condição** |  |
| **Proprietário** |  |

 

|  |  |
| --- | --- |
| **Campo** | *NJR\_CODREM* |
| **Sequência** | *001* |
| **Campo Domínio** | *NJR\_CODREM* |
| **Tipo** | *Primário* |
| **Regra** | *N96->N96\_DESREM* |
| **Posição?** | *SIM* |
| **Chave** | *xFilial('N96')+M->NJR\_CODREM* |
| **Condição** |  |
| **Proprietário** |  |
| **Campo** | *NJR\_CONDPA* |
| **Sequência** | *003* |
| **Campo Domínio** | *NJR\_DESREM* |
| **Tipo** | *Primário* |
| **Regra** | *N96->N96\_DESREM* |
| **Posição?** | *NÃO* |
| **Chave** | *xFilial('N96')+M->NJR\_CODREM* |
| **Condição** |  |
| **Proprietário** |  |

 

|  |  |
| --- | --- |
| **Campo** | *NJR\_CONDPG* |
| **Sequência** | *001* |
| **Campo Domínio** | *NJR\_DIASPG* |
| **Tipo** | *Primário* |
| **Regra** | *SY6->Y6\_DIAS\_PA* |
| **Posição?** | *SIM* |
| **Chave** | *XFILIAL('SY6')+M->NJR\_CONDPG* |
| **Condição** |  |
| **Proprietário** |  |

 

|  |  |
| --- | --- |
| **Campo** | *NJR\_CONDPG* |
| **Sequência** | *002* |
| **Campo Domínio** | *NJR\_DESPG* |
| **Tipo** | *Primário* |
| **Regra** | *MSMM(SY6->Y6\_DESC\_P,50)* |
| **Posição?** | *SIM* |
| **Chave** | *XFILIAL("SY6")+M->NJR\_CONDPG+STR(M->NJR\_DIASPG,AVSX3("NJR\_DIASPG",3))* |
| **Condição** |  |
| **Proprietário** |  |

 

Tabela **N7R – Rotas de Exportação**:

|  |  |
| --- | --- |
| **Campo** | *N7R\_CODROT* |
| **Sequência** | *001* |
| **Campo Domínio** | *N7R\_DESROT* |
| **Tipo** | *Primário* |
| **Regra** | SY9->Y9\_DESCR |
| **Posição?** | *NÃO* |
| **Chave** | xFilial("SY9")+M->N7R\_CODROT |
| **Condição** |  |
| **Proprietário** |  |

 

Tabela **N97 – Tp. Remessa x Modal Pág. Exp.**:

|  |  |
| --- | --- |
| **Campo** | *N97\_MODPAG* |
| **Sequência** | *001* |
| **Campo Domínio** | *N97\_DESMOD* |
| **Tipo** | *Primário* |
| **Regra** | EEF->EEF\_DESC |
| **Posição?** | *Sim* |
| **Chave** | xFilial('EEF')+M->N97\_MODPAG |
| **Condição** |  |
| **Proprietário** |  |

 

Tabela NNF - Despesas Corretores:

|  |  |
| --- | --- |
| **Campo** | NN7\_TIPCOM |
| **Tipo** | C |
| **Tamanho** | 1 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Título** | Dica Comis |
| **Descrição** | Tipo Comissão |
| **Inic. padrão** | 0 |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Navegar** | Não |
| **Opções** | 0 – Direta    1 – Um Remetro    2 – Conta Gráfica    3 – Deduzir da Fatura |
| **Quando** |  |
| **Relação** |  |
| **Val. Sistema** |  |
| **Ajuda** | Informe o tipo de Comissão :  0 – Direta  1 – Um Remetro  2 – Conta Gráfica  3 – Deduzir da Fatura |

 

|  |  |
| --- | --- |
| **Campo** | *N97\_DESMOD* |
| **Tipo** | *C* |
| **Tamanho** | *50* |
| **Decimal** | *0* |
| **Formato** | *@!* |
| **Título** | *Desc.Mod.Pág.* |
| **Descrição** | *Desc. Mod. Pág. Exp.* |
| **Nível** | *1* |
| **Usado** | *Sim* |
| **Obrigatório** | *Não* |
| **Navegar** | *Sim* |
| **Contras. padrão** | *(X3\_F3)* |
| **Opções** | *(X3\_CBOX)* |
| **Quando** | *(X3\_QUANDO)* |
| **Val. Sistema** | *(X3\_VÁLIDO)* |
| **Ajuda** | *Descrição da Modalidade de Pagamento Exportação.* |
| **Inic. padrão** | *IF(!INCLUI,POSICIONE('EEF',1,XFILIAL('EEF')+N97->N97\_MODPAG,'EEF\_DESC'),' ')* |
| **Inic. Navegar** | *POSIÇÃO('EEF',1,XFILIAL('EEF')+N97->N97\_MODPAG,'EEF\_DESC')* |

**6.**  *Criação ou Alteração* de **Parâmetros** no arquivo **SX6 – Parâmetros**:

|  |  |
| --- | --- |
| **Nome da Variável** | MV\_AGRO018 |
| **Tipo** | Lógico |
| **Descrição** | Parâmetro para indicar se o contrato compartilhado ou exclusivo |
| **Valor Padrão** | .F. |

 

MV\_AGRO018

##
