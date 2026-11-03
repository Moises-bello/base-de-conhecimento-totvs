---
article_id: 35330003727767
category: Financeiro
content_hash: 1d8608911f96ec2c050654fde332308c4c45bc45a20cd8a1143e2a5b57a0b8d0
fetched_at: '2026-06-28T22:38:03.207527+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA918 Conciliação
  de Pagamentos SITEF – Como funcionam as amarrações de pagamentos com múltiplos cartões
  MV_USAMEP=.T. para serem apresentadas na aba 'Conciliados'?
type: support-article
updated_at: '2025-10-01T15:08:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35330003727767-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA918-Concilia%C3%A7%C3%A3o-de-Pagamentos-SITEF-Como-funcionam-as-amarra%C3%A7%C3%B5es-de-pagamentos-com-m%C3%BAltiplos-cart%C3%B5es-MV-USAMEP-T-para-serem-apresentadas-na-aba-Conciliados
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35330049699223) Tempo aproximado para leitura: **00:15:00 min**  
  
**Dúvida**  
FINA918 Conciliação de Pagamentos SITEF – Como funcionam as amarrações de pagamentos com múltiplos cartões MV\_USAMEP=.T. para serem apresentadas na aba 'Conciliados'?  
  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
  
**Solução**  
Ao efetuar uma conciliação sitef com múltiplos cartões e essa não for apresentada na aba "Conciliados", iremos mostrar algumas amarrações que o sistema faz para trazer esse registro como 'conciliado'

Para pagamento com múltiplos cartões é obrigatório ter o parâmetro com o conteúdo **MV\_USAMEP = .T.**

Este exemplo estamos com as seguintes parametrizações:

**MV\_1DUP = 01**  
// Define a inicialização da 1ª parcela do título gerado. Ex: "A" para sequência alfabética, "1" para sequência numérica.

**MV\_BLADOC = .F.**  
// Define se a conciliação TEF considera o campo:  
// .F. = FIF\_NSUTEF  
// .T. = FIF\_NUCOMP

**MV\_USAMEP = .T.**  
// Indica se o sistema deve ignorar a tabela MEP para realizar a conciliação dos arquivos SITEF.

Cenário:

Na compra de uma pizza, eu e meu colega iremos dividir a conta. Logo será uma única compra, porém será paga em dois cartões

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35330003673367)

**Qual o motivo do campo ter gravado o mesmo conteúdo FIF\_PARCEL = 01?**

Pois faz parte de uma única compra (pizza)

**Como é feita a gravação da tabela SE1 para o exemplo acima?**

A tabela SE1 não pode gerar a mesma parcela igual ao conteúdo FIF\_PARCEL quando se tratar de uma única compra, pois iria apresentar chave duplicada, então gravada parcelas sequenciais conforme o exemplo da imagem acima.

**Como é feita as amarrações?**

Amarrações entre Campos – Conciliação SITEF no Protheus  
**1. Tabela FIF x SE1**

Relacionamento entre os campos da tabela de conciliação (FIF) e os títulos a receber (SE1):

FIF\_DTTEF = E1\_EMISSAO  
(Data do TEF é comparada com a data de emissão do título)

FIF\_TPPROD = E1\_TIPO  
(Apenas o primeiro conteúdo de FIF\_TPPROD é considerado para validação)

FIF\_CODFIL = E1\_MSFIL  
(Código da filial no FIF deve bater com o campo correspondente na SE1)

**Obs:** Identificação do Documento TEF (de acordo com o parâmetro MV\_BLADOC)

Quando **MV\_BLADOC = .F.**

FIF\_NSUTEF = E1\_NSUTEF  
(A validação não considera zeros à esquerda)

Quando **MV\_BLADOC = .T.**

FIF\_NUCOMP = E1\_DOCTEF  
(Também ignora zeros à esquerda na validação)

**2. Tabela SE1 x MEP**

Amarrações diretas entre os títulos a receber (SE1) e os registros da tabela MEP:

E1\_FILIAL = MEP\_FILIAL

E1\_PREFIXO = MEP\_PREFIX

E1\_NUM = MEP\_NUM

E1\_PARCELA = MEP\_PARCEL

E1\_TIPO = MEP\_TIPO

(Esses campos são usados para localizar o título correspondente na MEP)

**3. Tabela FIF x MEP**

Amarração da parcela entre FIF e MEP depende do tipo de sequência configurada no parâmetro MV\_1DUP:

Se MV\_1DUP for numérico:

FIF\_PARCEL = MEP\_PARTEF

Se MV\_1DUP for alfanumérico:

FIF\_PARALF = MEP\_PARTEF

---

Segue um trecho da documentação "[FINA918 - Conciliação de Pagamentos](https://tdn.totvs.com/pages/releaseview.action?pageId=655196877)"

**Relacionamento de campos SE1 x FIF x MEP para conciliação de pagamentos Software Express, Rede, Amex e Cielo.**

Para os registros aparecerem na aba **Conciliados**ou **Conciliados Parcialmente**os seguintes campos das tabelas **SE1**, **FIF**e **MEP**precisam ter o mesmo conteúdo.

|  |  |  |  |
| --- | --- | --- | --- |
| E1\_FILORIG | = | FIF\_CODFIL |  |
| E1\_DOCTEF | = | FIF\_NUCOMP | Se o MV\_BLADOC = .T. |
| E1\_NSUTEF | = | FIF\_NSUTEF | Se o MV\_BLADOC = .F. |
| E1\_PARCELA | = | MEP\_PARCEL | Se o MV\_USAMEP = .T. |
| MEP\_PARTEF | = | FIF\_PARCEL | Se o MV\_1DUP = A e MV\_USAMEP = .T. |
| E1\_PARCELA | = | FIF\_PARALF | Se o MV\_1DUP = A e MV\_USAMEP = .F. |
| E1\_PARCELA | = | FIF\_PARCEL | Se o MV\_1DUP = 1 e MV\_USAMEP = .F. |
| E1\_EMISSAO | = | FIF\_DTTEF |  |
| FIF\_CODAUT  FIF\_CODAUT  E1\_CARTAUT | =  =  = | E1\_CARTAUT  Em Branco  Em Branco | Verifica em ordem se alguma das condições atende para que o registro seja apresentado na aba conciliados. |

**Relacionamento de campos SE1 x FIF para conciliação de pagamentos PIX e Carteiras Digitais.**

Para os registros aparecerem na aba **Conciliados** ou **Conciliados Parcialmente**os seguintes campos das tabelas **SE1**e **FIF**precisam ter o mesmo conteúdo.

|  |  |  |
| --- | --- | --- |
| E1\_FILORIG | = | FIF\_CODFIL |
| E1\_DOCTEF | = | FIF\_NUCOMP |

**Relacionamento de campos FJU x FIF para conciliação de pagamentos PIX e Carteiras Digitais.**

Para os registros aparecerem na aba **Estornados**os seguintes campos das tabelas **FJU**e **FIF**precisam ter o mesmo conteúdo.

|  |  |  |
| --- | --- | --- |
| FJU\_EMIS | = | FIF\_DTTEF |
| FJU\_DOCTEF | = | FIF\_NUCOMP |

Saiba mais:

FINA911 – Justificativas TEF  
FINA918 – Conciliação de Recebimentos    
FINA916 – Conciliação de Vendas    
FINA914 – Importação    
FINA921 – Conexão com TOTVS Pagamentos Digitais
