---
article_id: 38684469040663
category: Originação de Grãos (OG)
content_hash: 1977236cbb7cb8657e83f43b989e35e8b1f32ce6b253505d6b9117eaf01849c6
fetched_at: '2026-06-28T22:45:37.567683+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Como a rotina AGRA930 utiliza Pontos de Entrada
  MVC
type: support-article
updated_at: '2026-03-23T12:09:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38684469040663-Agro-Linha-Protheus-AGR-Como-a-rotina-AGRA930-utiliza-Pontos-de-Entrada-MVC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38684463500567) Tempo aproximado para leitura: **00:02:30 min**  
  
**Dúvida**  
A rotina **AGRA930** permite a utilização de **Pontos de Entrada MVC**? Como funciona o framework **MVC** do **Protheus** nesta rotina e quais eventos de interface gráfica são acionados durante o processamento?  
  
**Ambiente**  
TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**  
Sim, a rotina **AGRA930** permite a utilização de **Pontos de Entrada MVC**.

**Como funciona o** *framework* **MVC na rotina AGRA930:**

O *framework* **MVC do Protheus** aciona os pontos de entrada automaticamente com base no **ID do Modelo de Dados** e nos métodos nativos da classe **FwFormModel**.

Na função de importação **A930IMPORT**, utilizamos o **FwLoadModel - AGRA930** para gravar os dados na tabela **NPX - Resultado da Análise**.

**Comportamento durante o processamento em lote:**

Como a função principal atua como uma rotina de processamento em lote via arquivo **TXT**, e não como uma tela de cadastro padrão, os eventos de interface gráfica como **VIEWDEF** ou **FORMLINEPRE** não são acionados durante o loop de importação.

**Eventos que funcionam normalmente:**

No entanto, os **eventos de validação e gravação**, como:

* **MODELPRE** (pré-validação do modelo)
* **MODELPOS** (pós-validação do modelo)
* **MODELCOMMITTS** (commit da transação com sucesso)
* **MODELCOMMITNTTS** (commit da transação sem sucesso)

Estes eventos **funcionarão normalmente** para cada linha processada no **A930IMPORT**.

**Observação sobre prints da issue:**

Foram adicionados prints da issue com a passagem por alguns eventos como exemplo do **PE** da rotina testada.

**Importante:**

* A rotina **AGRA930** utiliza o framework **MVC - Model-View-Controller** **do Protheus**
* Pontos de Entrada relacionados à **interface gráfica** (VIEW) **não são acionados** durante processamento em lote
* Pontos de Entrada relacionados ao modelo de dados **MODEL** funcionam normalmente
* O processamento em lote utiliza **arquivo TXT** como entrada de dados
* A gravação é feita através do **FwLoadModel - AGRA930** que carrega o modelo **MVC**
* Os dados são gravados na tabela **NPX - Resultado da Análise**
* Utilize os eventos **MODELPRE, MODELPOS, MODELCOMMITTS e MODELCOMMITNTTS** para customizações durante a importação
* Eventos como **VIEWDEF** e **FORMLINEPRE** só são acionados em telas de cadastro interativas
* Para validações customizadas, utilize preferencialmente os eventos **MODELPRE** e **MODELPOS**

![MVC.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38686072201751)![MVC1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38686028233495)![MVC2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38686028235415)![MVC3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38686028236951)![MVC4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38686028238231)![MVC5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38686028239127)![MVC6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38686072209303)![MVC7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38686072210071)![MVC8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38686072211095)
