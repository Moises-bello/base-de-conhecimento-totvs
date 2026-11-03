---
article_id: 360019722552
category: RH - Dissídio
content_hash: 3aff87bf760747995cded7c17fcb1bc73ab569d989299280c5a3ce43bd33a96b
fetched_at: '2026-06-28T22:43:43.284048+00:00'
product: protheus
section_id: 360003109132
source: central-protheus
title: RH - Linha Protheus - GPE - Como configurar o sistema para calcular as verbas
  do tipo valor, sem ID de cálculo no Dissidio Retroativo
type: support-article
updated_at: '2025-08-07T15:02:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019722552-RH-Linha-Protheus-GPE-Como-configurar-o-sistema-para-calcular-as-verbas-do-tipo-valor-sem-ID-de-c%C3%A1lculo-no-Dissidio-Retroativo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34015450738071)** Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Como configurar o sistema para calcular as verbas do tipo valor, sem ID de cálculo ou sem referência salarial?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões.  
  
**Solução**1) Para verbas que não possuem identificadores de cálculo, é necessário realizar a configuração de Verbas em Valor para dissídio, lembrando que o sistema **somente irá calcular as diferenças** para verbas com origem **G** ou **I**.

Será necessário atender TODOS os requisitos:  
A) Verba sem identificador de cálculo   
B) Verba em valor  
C) Verba com origem I ou G

**OBS:** Para verba calculada na folha através de customização, sem ID de cálculo e tipo Valor, a origem da verba deverá ser G ou I.

Anteriormente era necessário criar a Fórmula VALDISS, realizando a inclusão no cadastro de fórmulas para Roteiro. Hoje, incluímos a fórmula no padrão, conforme print do roteiro de cálculo FOL abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/13254305823767)

2) Habilite o campo **Recal.lan.vl**., pois por padrão o campo **RV\_VALDISS** vem desabilitado na rotina de Verbas, então é necessário entrar no Configurador e habilitá-lo;

3) No **Configurador,** entre na rotina **Base de dados** pelo caminho **>Base de dados >Dicionário >Base de dados,** localize a tabela **SRV;**  
![](http://tdn.totvs.com/download/attachments/286510081/image2017-8-28%2017%3A45%3A30.png?version=1&modificationDate=1503953526000&api=v2)

4) Localize o campo **RV\_VALDISS - Recal.lan.vl**:  
![](http://tdn.totvs.com/download/attachments/286510081/image2017-8-28%2017%3A46%3A23.png?version=1&modificationDate=1503953526000&api=v2)

5) Edite e na aba **USO** selecione a opção **USADO**:  
![](http://tdn.totvs.com/download/attachments/286510081/image2017-8-28%2017%3A47%3A45.png?version=1&modificationDate=1503953526000&api=v2)

6) Salve a alteração em modo EXCLUSIVO;

7) Entre na rotina Verbas pelo caminho **>Atualizações >Definições de Cálculo**, e altere as verbas em valor e sem ID que devem ser recalculadas, na aba **DISSIDIO RETROATIVO** e altere o campo **Recal. Lan. vl.** para **SIM**:  
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8379700728215)

8) Após todas as configurações acima, calcule o dissídio, o Sistema irá calcular a verba com a sua diferença de acordo com seu percentual aplicado:   
![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8379759533207)

**Saiba Mais:**[Artigos Dissídio](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109132-RH-Diss%C3%ADdio)
