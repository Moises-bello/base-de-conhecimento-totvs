---
article_id: 360035278333
category: GPE - eSocial - Não Periódicos
content_hash: 2757b73f4674dba115f516ccef4ce68cf265b808aeab907a61945eeb0a2d23e7
fetched_at: '2026-06-28T22:45:04.418198+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2190 - Como faço para gerar uma Admissão
  Preliminar (S-2190) do funcionário
type: support-article
updated_at: '2026-06-16T12:51:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035278333-RH-Linha-Protheus-GPE-eSocial-S-2190-Como-fa%C3%A7o-para-gerar-uma-Admiss%C3%A3o-Preliminar-S-2190-do-funcion%C3%A1rio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21617889360535) Tempo aproximado para leitura: 00:03:00 min**  
  
**Dúvida**  
Como faço para gerar uma **Admissão Preliminar** (S-2190) do funcionário?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**  
De acordo com o MOS (Manual de Orientação do eSocial) vigente:   
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9249182092183)

De acordo com o leiaute vigente, a *tag* <**matricula**> se tornou obrigatório:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9249387894935)

Para que a admissão preliminar seja localizada no eSocial quando enviada a admissão completa, **o campo matricula enviado no S-2190** deve ser o mesmo gerado no S-2200 ou S-2300. Por isso sugerimos que o cadastro do colaborador seja realizado **sempre no módulo SIGAGPE**, mantendo então a fidelidade da matricula e garantindo a integridade das informações.  
  
**ATENÇÃO**  
Não recomendamos realizar a admissão preliminar no TAF, pois ao realizar a admissão completa e integrar o evento S-2200 a partir do **SIGAGPE,** será criado uma matricula eSocial diferente da que consta no evento S-2190, e por consequência o trabalhador ficará com duas matriculas ativas no portal eSocial.  
  
**Procedimento:**  
É necessário que o parâmetro **MV\_EFDAVIS**, esteja com o conteúdo **0**. Desta forma, ao preencher o cadastro do funcionário e estiver faltando alguma informação obrigatória para o eSocial, será gerado uma mensagem de informação do campo que não foi preenchido e gerado o evento S-2190 para o TAF e ficando disponível o evento para transmissão ao eSocial.  
[RH - Linha Protheus - GPE - eSocial - Saneamento de Base - Como consultar, configurar ou alterar os parâmetros do Prothe](https://centraldeatendimento.totvs.com/hc/pt-br/articles/25252443928855-RH-Linha-Protheus-GPE-eSocial-Saneamento-de-Base-Como-consultar-configurar-ou-alterar-os-par%C3%A2metros-do-Protheus)   
  
Acessar a rotina do cadastro do colaborador em **Atualizações > Funcionários > Gestão Funcionários (ou Funcionários ou Contr. Individual)** e incluir o cadastro. Para o cadastrar uma preliminar, além dos campos obrigatórios é necessário informar os campos:

* CPF;
* Salário;
* Tipo de Contrato;
* Data término do contrato (quando contrato for por prazo Determinado).

Fechando a mensagem, apresentará outra mensagem dizendo que não foi preenchido todos os campos obrigatórios para o eSocial. Se deseja gerar o S-2190:

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9250747481111)

**Sim:** Fecha o cadastro e integra o S-2190.

**Não:** Fecha o cadastro sem integrar o registro.  
  
Ao utilizar a opção **sim** o sistema irá integrar o S-2190, o *browser* do TAF no cadastro do trabalhador deve apresentar a matricula a mesma informação gerada no cadastro do colaborador, no campo Cód. Único.

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9250936285335)

Para verificar **quais campos faltam preenchimento** para assim gerar o **evento S-2200**, utilize o menu **Miscelânea > eSocial > Carga Inicial**. Informe a matricula do funcionário em parâmetros (outras ações), deixe a pergunta **Retificar igual a não**. Dessa maneira o sistema irá gerar o *log* informando os campos que faltam.  
Consulte também o artigo: [RH - Linha Protheus - GPE - eSocial - S-2190 - Sempre tenho que enviar um evento de admissão preliminar (S-2190) antes de enviar o evento de admissão com os dados completos (S-2200)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018234511)   
  
**Acesse a nova funcionalidade** [**Geração S-2190 de forma automática**](https://tdn.totvs.com/pages/releaseview.action?pageId=1047378062)  
Com a obrigatoriedade da matrícula do eSocial no evento S-2190 - Admissão Preliminar, o código é preenchido manualmente no cadastro do TAF para geração do evento.

Para incluir posteriormente o mesmo trabalhador no SIGAGPE, como o código único é gerado automaticamente, fica divergente do código informado no TAF.

Sendo assim, esta funcionalidade visa permitir que o usuário busque a matrícula previamente cadastrada na rotina de Admissão Preliminar do TAF, informando o mesmo código no Cadastro de Funcionários do SIGAGPE.  
  
**Saiba Mais**  
Para saber mais consulte os *links* abaixo:   
[How To - S-2190](https://www.youtube.com/watch?v=q7yEUFoNM9k)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[Agenda de Eventos Tira Dúvidas Suporte](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-2-consolidada-ate-a-no-s-1-2-052023.pdf)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
