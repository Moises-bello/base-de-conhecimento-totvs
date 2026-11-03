---
article_id: 360018486631
category: Cadastros
content_hash: 802c575c2f8dcae7f3c29206bb63f476cb630c19e220295c93d4db60827ea619
fetched_at: '2026-06-28T22:46:28.512498+00:00'
product: rm
section_id: 1500000861582
source: central-rm
title: RH - RM - PTO - Como Inserir abono no espelho do funcionário
type: support-article
updated_at: '2026-02-11T11:29:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018486631-RH-RM-PTO-Como-Inserir-abono-no-espelho-do-funcion%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16503996124311) **Tempo aproximado para leitura: 00:01:00 min**

**Dúvida**  
Como cadastrar abono pela visão do espelho de ponto do funcionário?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto - A partir da versão 11.80  
  
**Solução**  
Para realizar da inserção de um abono para o funcionário, siga os passos abaixo:

1. Acesse a visão do espelho do funcionário e localize e clique sobre o dia da falta ou atraso do funcionário. No exemplo abaixo, verificamos na aba **Ocorrências** que fica disponível na janela de informações.    
   ![ocorrenca.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/29658877915287)
2. Para lançar o abono, acesse a opção **Anexos** e selecione a opção **Abono funcionário**.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/29658877918743)
3. A janela de anexo do **Abono funcionário** será aberta e clique no botão **Incluir**.  
     
   **Visão da nova gestão de Abono:** Nela é possível escolher se abono vai ser realizado por intervalo ou número de horas, na própria tela de abonar:  
   ![nova gestão de abnos.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/29658877926423)  
     
   Para maiores informações sobre a nova gestão de abonos acesse o artigo abaixo:  
   [RH - RM - PTO - Nova gestão de abonos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025539653)
4. **Visão da antiga de abonos, abono por intervalo**:  
   ![abono por intervalo_antiga.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/29658877927831)
5. **Visão da antiga visão de abonos, abono por número de horas**:  
   ![por numero de horas.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/29658877932183)  
     
   **Importante**:   
   1 - Por já ter sido selecionado o dia a ser abonado, os campos data início e data fim já virão previamente preenchidos, mas caso deseje é possível alterar a data.  
     
   3- Na nova gestão de abonos, somente é possível incluir o abono, caso já tenha falta ou atraso calculado, não é possível inserir abono para datas futuras.  
     
   2- Na antiga visão de abonos, a tela será apresentada com o campo por intervalo **Hora Início** e **Hora fim**, ou **Número de horas**, conforme exemplos acima. Estes campos dependem da parametrização de seu sistema.  Caso deseje alterar a visão da tela de abono, saia da visão do espelho de ponto acesse **Configurações** | **Parametrizador** e selecione o processo **Iniciais, e avance** até a está Abono e realize o ajuste da parametrização:  
   ![parametrização_inicial_abono.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/29658939954967)

   Ao habilitar o parâmetro **"Considera abonos por intervalo**" será necessário informar o intervalo de horas para se cadastrar um abono para o funcionário. Desabilitando este parâmetro o sistema trará como default no momento do cadastramento do abono, o número de horas de falta, ou atrasos que o funcionário possui naquele dia já calculado em sua movimentação.

   Observação: Ao utilizar o lançamento de abonos por intervalo é recomendado que esse parâmetro esteja marcado para que o sistema calcule corretamente os intervalos abonados.
6. Após o lançamento do abono, realize o recálculo do espelho do funcionário, para que os abonos sejam gerados.

**Saiba mais**  
Para maiores informações sobre as parametrizações de abonos, acesse a documentação:   
[Cadastro de Abonos](https://tdn.totvs.com/pages/releaseview.action?pageId=452719414)

[Parâmetros do Abono](https://tdn.totvs.com/pages/viewpage.action?pageId=452719531)
