---
article_id: 360051127413
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: f54fd4870886bd90dd087f9ce76d2ac1b06cd8e091317f2f0664b9415892b34c
fetched_at: '2026-06-28T22:42:11.842884+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Registro Tipo
  23 Quadro 02 > Valor dos CFOP de Serviços 5933 e 6933 Duplicado nas Colunas "Vlr
  Contábil" e "Outras".
type: support-article
updated_at: '2022-08-18T14:08:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051127413-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Registro-Tipo-23-Quadro-02-Valor-dos-CFOP-de-Servi%C3%A7os-5933-e-6933-Duplicado-nas-Colunas-Vlr-Cont%C3%A1bil-e-Outras
---

**Dúvida**Registro Tipo 23 Quadro 02 > Valor dos CFOP de Serviços 5933 e 6933 Duplicado nas Colunas "Vlr Contábil" e "Outras".  
   
 **Ambiente**  
Microsiga Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**  
Referente o erro mencionado no registro Tipo 23 Quadro 02 da DIME-SC, temos um parecer da nossa consultoria referente ICMS-SC:

"Caracteriza-se como Nota Fiscal Conjugada (mista) aquela na qual o valor contábil é sujeito, em parte, ao ICMS e em parte ao ISS, constando em um mesmo documento fiscal informações relativas à circulação de mercadorias e a prestação de serviços sujeitos à incidência do ISS, em quadro próprio inserido em espaço pré-determinado."  
  
Poderá ser utilizada em caso de NF eletrônica que contém apenas serviço, para atender ao relatório, utilizar um TES para o item Serviço com o campo "Calcula ISS" = "Não" , "L Fiscal ISS" = "Outros" e é obrigatório que tenha um código de serviço vinculado ao cadastro do produto no campo "Cod. Serv. ISS" (B1\_CODISS). Desta forma será criada a escrituração para a sua seja escriturado e utilizando a pergunta "Destaca Nts Serviço" no relatório MATR930 a NF conjugada será carregada corretamente.  
  
Conforme a resposta da consultoria tributária, mencionada acima, sugerimos a configuração orientada pela consultoria tributária e caso não atenda sua necessidade favor detalhar o impacto da configuração.

Abaixo link contendo parecer referente notas fiscais conjugadas:

<https://tdn.totvs.com/pages/releaseview.action?pageId=274304771>
