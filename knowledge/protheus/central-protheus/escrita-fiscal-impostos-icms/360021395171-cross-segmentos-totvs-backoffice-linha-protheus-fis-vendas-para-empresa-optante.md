---
article_id: 360021395171
category: Escrita Fiscal - Impostos - ICMS
content_hash: 614d22984f6ca08a6d67519c36faaec260a5e470d66798a8916edec12aeb98c1
fetched_at: '2026-06-28T22:39:26.025809+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Vendas para empresa
  optante do simples nacional com redução de base e desconto de ICMS conforme determina
  a Lei nº 7.014/96 do estado da BAHIA para operações internas
type: support-article
updated_at: '2021-07-20T14:13:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021395171-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Vendas-para-empresa-optante-do-simples-nacional-com-redu%C3%A7%C3%A3o-de-base-e-desconto-de-ICMS-conforme-determina-a-Lei-n%C2%BA-7-014-96-do-estado-da-BAHIA-para-opera%C3%A7%C3%B5es-internas
---

**Dúvida**

O Art. 16, alínea C da Lei nº 7.014/96 combinados com IN 38/94, no Estado da Bahia determina uma redução na alíquota nas vendas e remessas da indústria e a aplicação da alíquota de 7% do ICMS nas operações com mercadorias saídas de quaisquer estabelecimentos industriais situados neste Estado cujo imposto seja calculado pelo regime normal de apuração, destinadas a microempresas, empresas de pequeno porte e ambulantes, quando inscritas como tais no cadastro estadual, exceto em se tratando de mercadorias efetivamente enquadradas no regime de substituição tributária e de mercadorias consideradas supérfluas.

**Segue o trecho da Lei nº 7.014/96:**

Art. 16. Não se aplicará o disposto no inciso I do artigo anterior, quando se tratar das mercadorias e dos serviços a seguir designados, cujas alíquotas são as seguintes:  
I - 7% (sete por cento) nas operações com:

(...)  
c) mercadorias saídas diretamente do estabelecimento fabricante situado  
neste Estado com destino a empresas de pequeno porte e microempresas  
inscritas no cadastro estadual, exceto em se tratando das mercadorias  
enquadradas no regime de substituição tributária e das mercadorias não  
enquadradas no regime de substituição relacionadas nos incisos II, III e IV do  
caput deste artigo; Nota: A

(...)  
§ 1º A aplicação da alíquota de 7% (sete por cento), prevista na alínea “c” do inciso I do caput deste artigo, fica condicionada ao repasse para o adquirente da mercadoria, sob a forma de desconto, do valor correspondente ao benefício fiscal, devendo o desconto constar expressamente no documento fiscal.

O cliente possui alguns produtos com redução na base de cálculo conforme previsão legal contida no RICMS Título do documento - BA cumulada com a regra da aplicação da alíquota de 7% sobre os produtos remetidos do estabelecimento industrial destinados a empresas enquadradas no Simples Nacional na operação interna.

Foi aberto uma consulta no fisco baiano através do parecer nº 26.733/2013 onde é informado que o contribuinte Baiano pode aplicar a redução sobre a Base de Cálculo cumulada com a redução da alíquota de 7%, desde que a carga tributária seja 12% para 7% em vez de 17% para 7%, como se fosse em uma operação normal sem a redução de base de cálculo.

**Demonstrativo de cálculo efetuado pelo cliente.**  
CÁLCULO:  
Valor Produto: 16.904,60  
Redução de Base: 4.971,93 (16.904,60 x 29,4117%)  
Valor com redução: 11.932,67 (16.904,60 - 4.971,93)  
Desconto de ICMS: 641,54 (11.932,67 x 5.37634%) – Reduz parcialmente em 50% o fator fixo determinado na IN 38/94 10,75269  
Base de Cálculo ICMS: 11.291,14 (11.932,67 - 641,54)  
ICMS: 790,38 (11.291,14 x 7%)  
Valor do IPI: 483,74  
Valor da NF = 16.746,80 (16.904,60 – 641,54 + 483,74)  
Valor da NF = Valor dos produtos – Desconto + IPI

Atualmente o sistema não atende essa situação, será necessário efetuar o tratamento correto, para que o cliente possa informar o fator fixo para redução e desconto do ICMS e esse desconto ser aplicado após a redução de base de ICMS quando o produto tiver a mesma. Esse mesmo desconto de ICMS deve ser passadono valor final da nota.

Segue o parecer da consultoria tributária:  
<http://tdn.totvs.com/pages/releaseview.action?pageId=215484104>

**Ambiente**Todas as versões  
  
   
**Solução**

Venda para cliente do estado da BA, com redução de base do ICMS no produto e mais desconto do ICMS:

- Parâmetro SX6: MV\_ESTADO = BA;

- Cliente: (A1\_EST) = BA;  
(A1\_SIMPNAC) = SIM;  
  
- Produto: (B1\_PICM) = 7%;

Obs.: a alíquota também poderá ser configurada através das exceções fiscais conforme orientado no link abaixo:

<http://tdn.totvs.com/pages/releaseview.action?pageId=142813099>

- TES: (F4\_ICM) = SIM;  
(F4\_BASEICM) = 70,5883 - correspondente ao valor de 29,4117%;  
(F4\_FTRICMS) = 5,37634 – Reduz parcialmente em 50% o fator fixo determinado na IN 38/94 10,75269

Na geração da nota fiscal de saída o sistema efetuara o seguinte cálculo:

Valor Produto: 16.904,60  
Redução de Base: 4.971,93 (16.904,60 x 29,4117%)  
Valor com redução: 11.932,67 (16.904,60 - 4.971,93)  
Desconto de ICMS: 641,54 (11.932,67 x 5.37634%) – Reduz parcialmente em 50% o fator fixo determinado na IN 38/94 10,75269  
Base de Cálculo ICMS: 11.291,14 (11.932,67 - 641,54)  
ICMS: 790,38 (11.291,14 x 7%)  
Valor do IPI: 483,74  
Valor da NF = 16.746,80 (16.904,60 – 641,54 + 483,74)  
Valor da NF = Valor dos produtos – Desconto + IPI

Os valores serão gravados nos seguintes campos:

Tabela SD1:  
D1\_FTRICMS - Fator de Redução Desc. ICMS  
D1\_VRDICMS - Valor de Redução Desc. ICMS

Tabela SD2:  
D2\_FTRICMS - Fator de Redução Desc. ICMS  
D2\_VRDICMS - Valor de Redução Desc. ICMS

Tabela SFT:  
FT\_VRDICMS - Fator de Redução Desc. ICMS  
FT\_FTRICMS - Valor de Redução Desc. ICMS
