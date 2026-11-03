---
article_id: 10095259240727
category: Rescisão
content_hash: 61eb38734a9ae9e7b114a708a1e8986699f12ddd018ff7d7dfb403cabcc50201
fetched_at: '2026-06-28T22:46:54.305895+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: RH - RM - FOP - Geração GRRF
type: support-article
updated_at: '2024-09-16T18:20:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10095259240727-RH-RM-FOP-Gera%C3%A7%C3%A3o-GRRF
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23510727801623)**Tempo aproximado para leitura: **7min 45sec**

**Dúvida**Qual o passo a passo para a Geração da GRRF?**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para solucionar essa dúvida, acesse: menu **Rescisão | GRFC/GRFF** para acessar a rotina. Na rotina de GRRF você encontrará diversos campos parametrizáveis, conforme imagem abaixo. Verifique a descrição de cada campo e faça sua parametrização conforme necessário.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23510898406551)

* **Competência:** Refere-se ao período, mês e ano em que o usuário deseja buscar os dados da GRRF.
* **Dissídio Sim ou Dissídio Não:** Este campo indicará se a GRRF é devido ao pagamento de dissídio pela empresa. Quando o dissídio for sim, deverá cadastrar os dados do dissídio. Quando for não, basta informar no campo.
* **Ind. Correção FGTS:** No campo "Ind. Correção FGTS" deve ser informado o índice de correção conforme tabela liberada pela CEF para o cálculo sobre o valor do dissídio. Este índice ficará gravado de acordo com o perfil e quando o usuário for gerar outra GRRF sem correção deverá limpar os dois campos,(mais informações nas documentações no saiba mais).
* **Não enviar dados do Banco de pagamento do funcionário:**Caso marcado, esse campo não ira levar as informações do banco do funcionário para o documento.
* **Recolhimento Centralizado(CNPJ Matriz):** Caso a empresa faça o recolhimento de FGTS centralizado o parâmetro deve ser marcado, para que o CNPJ da centralizadora seja informado no arquivo.
* **Quebra de arquivo para cada tomador de serviço do funcionário:** Marcando esse campo o layout do arquivo final será divido por tomadores de serviço de acordo com a quantidade informada para cada funcionário.
* **Desconsiderar o acréscimo de 10% na multa de FGTS:** Quando marcado, não será gerado o acréscimo de 10% da multa rescisória, (mais informações nas documentações no 'saiba mais').

* **Localização do arquivo:**Este campo se refere ao local no computador em que será salvo o arquivo após a finalização da geração.

Após finalizar a primeira tela de parametrizações você será encaminhado para a segunda que deve ser preenchida com os dados da empresa:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23510937871895)

Na próxima etapa você será levado para 'Seleção de Coligadas', após selecionar a coligada você tem a opção de parametrizar novamente, podendo afunilar ainda mais a sua geração, segue:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23510898425111)

Caso opte por usar os parâmetros específicos de coligada, você será encaminhado para a tela a baixo, verifique a descrição de cada campo e faça sua parametrização conforme necessário.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23510898437911)

* **Usar parâmetros:** Caso opte por usar os parâmetros específicos da coligada esse campo deve ser marcado.
* **Seleção de funcionários:**Nesta seleção de funcionários diferente da primeira, você poderá selecionar apenas um funcionário.
* **Fórmula Para Cálculo de Horas Semanais:** Esse campo, se utilizado, o resultado da fórmula terá prioridade sobre o cálculo interno utilizado pelo sistema. Caso contrário o sistema utilizará o calculo interno (jornada mensal dividido por 5).Os outros parâmetros a baixo, terão os mesmo propósitos dos que foram citados na primeira tela porém caso sejam marcados agora irão ser aplicados somente para a coligada que foi selecionada nos parâmetros específicos.  
    
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/23510898449943)  
    
  Caso opte por gerar lançamentos financeiros que levem a GRRF, basta marcar a opção a baixo e parametrizar o lançamento financeiro conforme desejado.  
    
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/23510898460183)

**Saiba Mais**  
[GRRF - Guia de Recolhimento Rescisório do FGTS](https://tdn.totvs.com/pages/releaseview.action?pageId=452719518)

[Contribuição Social](https://tdn.totvs.com/pages/releaseview.action?pageId=527841168)

[Geração GRRF](https://tdn.totvs.com/pages/releaseview.action?pageId=311065074)
