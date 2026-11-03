---
article_id: 4403852850583
category: Faturamento - Cadastros
content_hash: 11c9618bb055382c462432243c8d658a94fa86be982b64b7e709c764f456bc2a
fetched_at: '2026-06-28T22:38:35.343797+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Sequencial do
  código do cliente
type: support-article
updated_at: '2022-11-16T20:53:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403852850583-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Sequencial-do-c%C3%B3digo-do-cliente
---

**Dúvida**

Como gerar um sequencial para o código do cliente (**mata030**)?   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.  
  
**Solução**

Por padrão, o código do cliente deve ser digitado manualmente, alguns clientes utilizam validações para trazer a próxima numeração automaticamente, como o uso do **GETXENUM.** Para esse tratamento é preciso incluir a sintaxe no **inicializador** **padrão** do campo **A1\_COD**:

```
GetSxeNum("SA1","A1_COD")
```

Desta forma, o sistema irá sugerir o próximo número do código do cliente automaticamente, com base na estrutura do licence server. Todavia, como o fonte não está totalmente preparado para tratar essa validação, pode ocorrer vários erros como pular numeração, chave duplicada e não trazer a próxima numeração.

Veja nosso vídeo a respeito do assunto no YouTube: [**Ajuste de Numeração automática das tabelas**](https://youtu.be/BhEo-9FFUIQ)  
  
Para este caso, o procedimento orientado pela TOTVS é o de uso do ponto de entrada para criar uma validação de busca da numeração: **[CriaSXE - Controle de Numeração](https://tdn.totvs.com/pages/releaseview.action?pageId=6815179)**

**Importante**

Esta configuração no SX3 para geração automática de numeração sequencial deve ser utilizada apenas por campos nos quais já consta a definição no nativo do Protheus. Não deve ser incluída manualmente em campos que não possuem este controle automático por padrão (como por exemplo no campo C5\_NUM). Isto porque, este tratamento por si só não trata abandono de numeração reservada não utilizada (este tratamento é realizado no código fonte das rotinas). Ou seja, ao reservar a próxima numeração clicando em "Incluir"(registro 000010 por exemplo) mas não efetivar a gravação, abandonando o registro, depois de já ter sido utilizada a numeração seguinte (depois de outra instância ter gravado a 000011 por exemplo) serão provocadas lacunas fazendo com que o controle automático se perca. Desta forma, seria necessário verificar a possibilidade de uso de ponto de entrada na rotina que deseja implementar o uso de numeração automática para o fiel comportamento da ferramenta, de forma a tratar abandonos de reserva de numeração.

**Saiba mais:**

**[GetSXENum - Último sequencial do campo da tabela](https://tdn.totvs.com/x/zfxn)**

**[FAT0046 Ajuste de Numeração automática dos Formulários (Tabelas / ALIAS) no Protheus](https://tdn.totvs.com/pages/viewpage.action?pageId=235570751)**

**[MP - FAT - O código sequencial do cadastro de cliente Vtex não segue o Padrão do Protheus. Como validar os campos A1\_COD e A1\_LOJA na integração.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000433221-MP-FAT-O-c%C3%B3digo-sequencial-do-cadastro-de-cliente-Vtex-n%C3%A3o-segue-o-Padr%C3%A3o-do-Protheus-Como-validar-os-campos-A1-COD-e-A1-LOJA-na-integra%C3%A7%C3%A3o-)**

**[MP - FAT - Como o Protheus cria e grava um Código de Cliente na Integração EAI](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048507313-MP-FAT-Como-o-Protheus-cria-e-grava-um-C%C3%B3digo-de-Cliente-na-Integra%C3%A7%C3%A3o-EAI)**

**[MP-FAT- Uso Função A030INICPD()](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061201674-MP-FAT-Uso-Fun%C3%A7%C3%A3o-A030INICPD-)**
