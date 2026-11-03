---
content_hash: a8a87c54637579b3da0ff5f2456a5df2ff4deb1d4523f2dfff49e867eb07f4b7
fetched_at: '2026-06-29T00:10:19.231430+00:00'
page_id: '4813132'
product: rm
source: tdn-rm
title: CTRC - Conhecimento de Transporte de Saída
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=4813132
version: 6
---

BLOCK

CTRC - Conhecimento de Transporte de Saída

FAQ: **CTRC - Conhecimento de Transporte de Saída**

Avaliação

* ***Como Fazer***

Como parametrizar o sistema para utilizar Conhecimento de Transporte em Movimentações de Saída?

* ***Definição do Processo***

Utilizada pela unidade fiscalizadora para verificar a veracidade das mercadorias descritas na Nota Fiscal com as mercadorias Transportadas(descritas na NF de Conhecimento de Transporte).

Para utilização do CTRC é necessário que sejam inclusos dois tipos de movimento um para emissão das notas fiscais e outro responsável pela emissão do CTRC.

Solução

* ***Parametrizações Necessárias***

> ***Parametrização do movimento de “EMITIR CTRC******”***

Acessar | **Opções | Parâmetros | RMNucleus |** e selecionar processo onde o tipo de movimento a ser utilizado para este fim foi configurado. A seguir editar o mesmo e informar:

**Etapa Fis – Dados (Versões antigas)**

- Usar CTRC : Emitir CTRC

**Etapa Fis – Conhecimento de transporte (Versões mais atuais)**

- Tipo de Operação do Conhecimento de Transporte : Emitir CTRC

**Etapa Mov – Transporte**

- Tipo de Frete | CIF/FOB : Edita

**Etapa Fis – Natureza**

- Natureza | Edição : Edita |

- Seleção Automática da Natureza : definir tipo de seleção da natureza

\*\*Parametrização específica para geração de lançamentos fiscais\*\*

**Etapa Fis – Escrituração**

- Gerar Escrituração: habilitar

- Tipo Documento Escrituração | Código Default : informar tipo de documento que possua “Código do Modelo do Documento : 08”

- Tipo do Lançamento Fiscal da Transferência: Saída

\*\*Parametrização específica para geração de lançamentos fiscais\*\*

**Etapa Fis – Tributação**

Incluir e parametrizar os tributos de forma que atenda aos dados a serem apresentados no item ou movimento

\*\*Parametrização específica para geração de lançamentos fiscais\*\*

> ***Parametrização do movimento de “Nota Fiscal”***

Acessar | **Opções | Parâmetros | RMNucleus |** e selecionar processo onde o tipo de movimento a ser utilizado para este fim foi configurado. A seguir editar o mesmo e informar:

**Etapa Fis – Dados (Versões antigas)**

- Usar CTRC : Não Usar CTRC

**Etapa Fis – Conhecimento de transporte (Versões mais atuais)**

- Tipo de Operação do Conhecimento de Transporte : Não Usar CTRC

**Etapa Mov – Transporte**

- Tipo de Frete | CIF/FOB : Edita

**Etapa Fis – Natureza**

- Edição : Edita

- Seleção Automática da Natureza : definir tipo de seleção da natureza

\*\*Parametrização específica para geração de lançamentos fiscais\*\*

**Etapa Fis – Escrituração**

- Gerar Escrituração: habilitar

- Tipo Documento Escrituração | Código Default : informar o tipo de documento que deve ser apresentado no RMLIBER durante após escrituração |

- Tipo do Lançamento Fiscal da Transferência: Saída

\*\*Parametrização específica para geração de lançamentos fiscais\*\*

**Etapa Fis – Tributação**

Incluir e parametrizar os tributos de forma que atenda aos dados a serem apresentados no movimento

\*\*Parametrização específica para geração de lançamentos fiscais\*\*

* ***Descrição do Processo***

> ***Movimento de Nota Fiscal***

A movimentação de nota fiscal será inclusa como de costume, sendo considerado “Tipo do Frete” preenchido na aba **| Transporte |** do movimento. O valor líquido do movimento será considerado no momento da integração como o movimento de “emissão do CTRC”.

> ***Movimento de “Emissão de CTRC”***

A movimentação de “Emissão de CTRC” será feita como de costume, tendo como particularidade o preenchimento dos campos apresentados nas abas | Transporte e CTRC |

**Aba Transporte**

Informar tipo de frete pertinente movimentação, para termos de CTRC deverá ser do tipo FOB.

**Aba CTRC Dados do Transporte**

Esta aba deve ser preenchida quando houver dados de coleta x entrega da mercadoria, observando que, a informação preenchida nos campos **| Estado – Município |** de coleta e entrega vão interferir diretamente na seleção da natureza de operação(se utilizar), onde será obedecida hierarquia abaixo:

1ª Hierarquia: A seleção da natureza de operação será feita obedecendo UF da Coleta e UF da Entrega preenchidos na aba **| CTRC | Dados de Transporte | Local de Coleta |** se:

- Lançamento Fiscal estiver vinculado a um documento do tipo CTRC

- O destinatário da mercadoria preenchido na aba | Remetente e Destinatário | não for “Exterior”

Onde:

- Se a UF da Coleta = UF da Entrega: Utiliza: Utiliza Natureza Interna (5.XXX);

- Se a UF da Coleta <> UF da Entrega: Utiliza Natureza Interestadual (6.XXX);

2ª Hierarquia: A seleção da natureza de operação será feita obedecendo estado do Cli\for preenchida na aba **| Transporte | Cli\For Origem /Destino |** do movimento;

3ª Hierarquia: A seleção da natureza de operação será feita obedecendo estado do Cli\for preenchido na aba **| Identificação | Cliente \ Fornecedor |**

**Aba CTRC Saída**

A associação entre nota fiscal e CTRC será feita no tipo de movimento parametrizado para “Emitir CTRC”, onde o usuário deverá informar os dados das notas fiscais de saída que serão vinculadas ao mesmo.

A associação pode ser feita através do ícone **| [![clip_image002](http://lh5.ggpht.com/_G7KXZLoZDsY/TKtp_tdL6lI/AAAAAAAABwg/DEbzsTaFzwE/clip_image002_thumb.jpg?imgmax=800 "clip_image002")](http://lh3.ggpht.com/_G7KXZLoZDsY/TKtp-1N0shI/AAAAAAAABwc/Zpf6i1R4L_E/s1600-h/clip_image002%5B3%5D.jpg) Nota Fiscal de Terceiro |** onde o usuário vai preencher as informações da nota fiscal manualmente. Outra alternativa, é através do ícone **| [![clip_image004](http://lh5.ggpht.com/_G7KXZLoZDsY/TKtqA256MYI/AAAAAAAABwo/sn1gFr-Dljk/clip_image004_thumb.jpg?imgmax=800 "clip_image004")](http://lh5.ggpht.com/_G7KXZLoZDsY/TKtqAF_5HQI/AAAAAAAABwk/A9EnrtvFMTA/s1600-h/clip_image004%5B3%5D.jpg) Associar Notas Fiscais |** onde será aberta outra tela para que seja feito filtro das movimentações de nota fiscal que serão associadas a este CTRC.

* ***Informações Adicionais***

- O sistema não faz validação entre o valor do movimento de CTRC com o valor das notas fiscais vinculadas ao mesmo.

* ***Escrituração do Movimento de CTRC***

A escrituração dos movimentos será feita como de costume onde o usuário dever acessar **| Opções | Escrituração de Lançamentos – RMLIBER |** e fazer o filtro das movimentações de nota fiscal e escriturá-las. A seguir escriturar a nota de CTRC

Depois de concluído processo de escrituração, ao acessar o RMLIBER em **| Cadastro | Manutenção de Lançamentos de Saída |** e editar o lançamento fiscal de CTRC serão apresentadas informações do conhecimento de transporte na aba **| Dados do Transporte | CTRC | Notas Fiscais que Acobertam a Carga Transportada |**. Nesta aba serão apresentadas informações das notas fiscais vinculadas ao CTRC, ressaltando que a rotina de escrituração pertence ao aplicativo RMLIBER.

Para maiores informações:

Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/Rpt/Rpt.Reports.aspx)

**COMUNIDADE **[R@Materiais e Finanças](https://totvs.byyou.com/?space=rmateriais)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015
