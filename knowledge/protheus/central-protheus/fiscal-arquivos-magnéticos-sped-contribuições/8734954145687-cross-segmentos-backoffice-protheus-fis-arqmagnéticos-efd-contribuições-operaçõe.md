---
article_id: 8734954145687
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: 2254a6cfd432a08967b8752dd85a290c39ee75b8fe0539a3853feed676051cc1
fetched_at: '2026-06-28T22:42:06.671239+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições,
  operações de saídas com CFOP 5.949/ 6.949/ 7.949 não são geradas no arquivo txt.
type: support-article
updated_at: '2026-03-26T19:27:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8734954145687-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-opera%C3%A7%C3%B5es-de-sa%C3%ADdas-com-CFOP-5-949-6-949-7-949-n%C3%A3o-s%C3%A3o-geradas-no-arquivo-txt
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39320502019863) Tempo aproximado para leitura: 00:02:00 min  
  
**Dúvida**  
Informações sobre as operações de saída com o **CFOP** **final 949 (5.949/ 6.949/ 7.949)** na **Apuração** e no **arquivo txt** do **EFD Contribuições**.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**  
A tratativa de todas as Notas com o **CFOP** final **949** **(5.949/ 6.949/ 7.949)** serão conforme abaixo:  
  
- Nas **NF** com **CST 01 à 09**, o sistema considerará automaticamente essas **Notas** na **Apuração** e **Arquivo**.  
- Nas **NF** com **CST 49** não serão consideradas na **Apuração** e consequentemente no **arquivo magnético**.    
  
Foi ajustado a rotina para verificar o **CFOP 5949/6949 e os CSTs** que geram receita gerar os registros de notas fiscais não sendo necessário a **inserção dos CFOPs 5949 e 6949** nos parâmetros **MV\_CFAREC, MV\_CFEREC** e **MV\_CFNREC** . Foi efetuada a validação de **CFOP + CST** que geram **receita "01/02/03/04/05/06/07/08/09".**

Segue retorno na integra, do **Desenvolvimento da Totvs** sobre este assunto:

As operações com a CFOP 5949/ 6949/ 7949 representa outras saída de mercadoria ou prestação de serviço não especificado, ou seja, operações muito abrangentes que podem ser representativa de Receita ou não.  
O tratamento no sistema para esta CFOP era lógico e determinava se operação com esta CFOP eram geradoras de Receita ou não. Porém este cenário não era aderente as normas tributária em diversos cenários, assim foi necessário fazer um ajuste no sistema para o tratamento desta CFOP para ser aderente tanto as operações geradores de receita quanto as operações não geradoras de receita.  
Pela ISSUE *DSERFIS1-10569,* ajustamos a rotina para verificar o *CFOP 5949/6949/7949 e os CST's* que geram Receita gerar os registros de notas fiscais não sendo necessário a *inserção dos CFOPs 5949 e 6949* nos parâmetros *MV\_CFAREC, MV\_CFEREC* e *MV\_CFNREC* .  
Foi efetuada a validação de *CFOP + CST* que geram R*eceita "01/02/03/04/05/06/07/08/09".*  
Entendemos que alteração feita esta em consonância com as disposições legais e de acordo com as orientações da nossa consultoria de segmentos.   
É importante salientar que o próprio Guia Prático, orienta o contribuinte e enviar todas as notas fiscais, seja ela geradora ou não de crédito ou débito, devido a transparência das informações perante ao fisco.  
  
Com base em legislação, *link* da **Consultoria de Segmentos**.  
[*http://tdn.totvs.com/pages/releaseview.action?pageId=233754222*](http://tdn.totvs.com/pages/releaseview.action?pageId=233754222)
