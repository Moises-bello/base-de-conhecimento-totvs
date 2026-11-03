---
article_id: 360053791393
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: aa5557176f1e4717acc83c6deae8ee3d22791549ea93c33d86ef28dce2c86371
fetched_at: '2026-06-28T22:42:10.401964+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Configuração
  para o benefício Isento ser considerado no relatório DUB ICMS (FISR001)
type: support-article
updated_at: '2022-08-17T19:43:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053791393-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Configura%C3%A7%C3%A3o-para-o-benef%C3%ADcio-Isento-ser-considerado-no-relat%C3%B3rio-DUB-ICMS-FISR001
---

**Dúvida**Qual a configuração para que o benefício Isento seja considerado no relatório DUB ICMS?

**Ambiente**

Microsiga Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**É importante frisar que para a operação ser eleita para entrar com valor no relatório FISR001, é necessário que o campo de "Calcula ICMS" (F4\_ICM) no cadastro de TES esteja como "S -Sim" e o "L.Fisc.ICMS" (F4\_LFICM) como "I - Isento" ou "O - Outros", dessa forma a operação estará correta, pois terá o cálculo de ICMS que servirá para o relatório e não irá gerar débitos ou créditos no Livro Fiscal.

**Isenção**  
No caso de operações na quais a nota fiscal for escriturada com Isenta, o valor do ICMS que deixou de ser debitado/recolhido será considerado na impressão do relatório para esse tipo de benefício. Para isso o campo L. Fisc. ICMS (F4\_LFICM), no cadastro de TES, deve ser preenchido com conteúdo igual a I = Isento.

**Tipo DUB (F4\_TIPODUB)** - Indica o Tipo do Ato Legal utilizado no DUB-ICMS.

1=Convênio;  
2=Lei;  
3=Decreto;  
4=Protocolo;  
5=Resolução;  
6=Portaria.

**Benefic. DUB (F4\_BENDUB)** - Indica a Espécie do benefício utilizado no DUB-ICMS.  
3=Isenção;

**Num./Ano DUB (F4\_NUMDUB)** - Indica o Número de identificação do Ato Legal e o Ano de Publicação utilizado no DUB-ICMS. Deve ser preenchido com o Número do Ato Legal / Ano do Ato Legal. Exemplo: 12345/2008.

Informações adicionais:

<https://tdn.totvs.com/pages/releaseview.action?pageId=195297491>

<https://tdninterno.totvs.com/pages/releaseview.action?pageId=557344795>

DUB-ICMS - Alíquota - Operações com Produtos de Importação RJ  
<https://tdn.totvs.com/pages/releaseview.action?pageId=561847819>
