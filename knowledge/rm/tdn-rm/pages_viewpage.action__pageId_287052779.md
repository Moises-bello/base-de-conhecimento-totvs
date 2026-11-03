---
content_hash: 5197fab1c523b170579e1bf87dab53f705385414c2745a8967dc0287a3d11232
fetched_at: '2026-06-29T00:08:42.124694+00:00'
page_id: '287052779'
product: rm
source: tdn-rm
title: DT Adequação ao Leiaute 2.3
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=287052779
version: 100
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Folha de Pagamento |
| **Função:** | Adequação ao Leiaute 2.3 do eSocial |
| **Situação/Requisito:** | Adequar campos da base conforme leiaute 2.3 do eSocial. |
| **Solução/Implementação:** | 1-Número do Processo- S-1005, S-1020 e S-1070    Alterada a validação do campo 'Número do Processo' . A partir do leiaute 2.3 só serão listados os processos que tiverem o indicativo da matéria do processo ou alvará judicial, classificado como Tributária ou relativa ao FGTS.    Seleção do Processo Judicial:  Obs:   * O lookup de processo RAT  e FAT que busca o processo do Vitae no cadastro de seção passou a filtrar o indMatProc = 1 * O Campo código de suspensão passou ser obrigatório na tela o no XML.   2- Indicativo de Cooperativa- S-1000  Alterada a validação para o campo Indicativo de Cooperativa.  Validação: O preenchimento do campo é exclusivo e obrigatório para Pessoa Jurídica.  Somente pode ser diferente de ZERO se a Natureza Jurídica (natJurid) for igual a 2143 e Classificação Tributária (classTrib) for igual a [06, 07, 13, 99].  Para Classificação Tributária (classTrib) igual a 06 e 07 o campo deverá ser preenchido apenas com [0,2].  Valores Válidos: 0, 1, 2, 3.        Caso seja informada classificação tributária diferente de 06, 07, 13, 99, para indicativo de cooperativa  diferente de ZERO e natureza jurídica 214-3, o  sistema apresentará a seguinte mensagem:        3- Solicitação de Totalização para Pagamento em Contingência - S-1295  Criado  evento S-1295, que será utilizado como solução de contingência para o caso da empresa não conseguir fazer o fechamento dos eventos periódicos através do S-1299 (Fechamento dos Eventos Periódicos).        4- Conforme determinação do leiaute 2.3, foi retirada da tela e do XML as "Informações de repasse financeiro".  Antes:    Depois:    5- Conforme determinação do leiaute 2.3, o evento S-2100 foi extinto, sendo substituído integralmente pelo evento S-2200.  Consulte através do link abaixo, todos os campos do evento S-2200.  <http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.S2200.aspx>  Antes:    Depois:      6- Criação de novos Indicadores de cumprimento de aviso prévio   O leiaute 2.3, inclui 2 novos tipos de indicador de aviso prévio, além de alterar a validação do campo.  Indicadores criados:  3 - Outras hipóteses de cumprimento parcial do aviso prévio;  4 - Aviso prévio indenizado ou não exigível.  Antes:    Depois:    Validação: Informação obrigatória se as condições mencionadas a seguir ocorrerem simultaneamente:  a) Motivo de desligamento = [02, 03, 04, 07];  b) houve envio do evento S-2250 relativo à matrícula do empregado;  c) não houve preenchimento do grupo cancelamento do aviso prévio do último evento S2250 enviado relativo à matrícula do empregado;  d) a data do campo data de desligamento for igual ou anterior a data prevista do desligamento  e) último evento S-2250 relativo à matrícula do empregado.    7- Nível de Estágio  Foi incluído dois novos níveis de estágio:  8 - Especial;  9 - Mãe social. (Lei 7644, de 1987).    Antes:    Depois: |
| **Conversores e Parâmetros:** |  |
| **Tickets relacionados:** |  |
| **Requisito:** |  |

divs
