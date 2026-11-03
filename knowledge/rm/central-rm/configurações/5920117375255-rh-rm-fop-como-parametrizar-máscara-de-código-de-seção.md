---
article_id: 5920117375255
category: Configurações
content_hash: afe78feba08387efa007c6df2a1b31df4f3b5ab4c44b0beb086094c3ee9b6ee6
fetched_at: '2026-06-28T22:46:49.522230+00:00'
product: rm
section_id: 1500000834621
source: central-rm
title: RH - RM - FOP - Como parametrizar máscara de código de Seção.
type: support-article
updated_at: '2025-03-12T10:03:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5920117375255-RH-RM-FOP-Como-parametrizar-m%C3%A1scara-de-c%C3%B3digo-de-Se%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Como parametrizar Máscara de código de Seção?  
 **Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**A máscara de seção a ser definida, servirá para padronizar os códigos de seções que serão cadastradas.  
  
**Exemplo**  
Ao colocar uma máscara ##.##, o sistema irá permitir a inclusão apenas para código de seção numérico, como 01.01.  
   
**Importante**  
O campo máscara de seção será obrigatória. Caso o usuário não tenha cadastrado este campo em sua base de dados, deverá faze-lo logo que acessar o sistema. Ele deverá preencher o campo Máscara de código de seção conforme estrutura do cadastro de seções, veja exemplo abaixo:  
  
**Caminho | Configurações | Parametrizador | Marcaras e Quebras.**  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5920424749975/mceclip3.png)  
  
**Exemplo**  
01 Matriz  
01.01 Depto pessoal  
01.02 Depto.Contábil  
02 Filial Rio de Janeiro  
02.01 Depto pessoal  
02.02 Depto Contábil  
   
Neste caso, a máscara informada deverá ser = **##.##**

**Código de quebra mestre**  
 Informe, aqui, o código de quebra mais utilizado, que será assumido como padrão pelo sistema. Em qualquer relatório que não for informada a quebra, o RM Labore irá considerar o código de quebra mestre.

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5920489446167/mceclip4.png)  
 **Código de quebra para CNPJ**  
 Informe um código de quebra de forma a refletir as quebras desejadas de seções para os fins de totalizações em relatórios e lançamentos no sistema.  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5920514728343/mceclip5.png)

**Saiba mais****[Máscaras para os cadastros](https://tdn.totvs.com/pages/releaseview.action?pageId=452719891)**
