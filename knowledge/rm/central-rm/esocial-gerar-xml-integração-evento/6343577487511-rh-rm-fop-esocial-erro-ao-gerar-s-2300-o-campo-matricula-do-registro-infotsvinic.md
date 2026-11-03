---
article_id: 6343577487511
category: eSocial - Gerar XML/ Integração Evento
content_hash: 10e5039fbc447ab5eb2307babee1089ad96bc05725d04324c998a9ce92bc89c1
fetched_at: '2026-06-28T22:47:12.213595+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro ao gerar S-2300: O campo ''matricula'' do registro
  ''infoTSVInicio'' é obrigatório e não está preenchido'
type: support-article
updated_at: '2024-06-26T15:08:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6343577487511-RH-RM-FOP-eSocial-Erro-ao-gerar-S-2300-O-campo-matricula-do-registro-infoTSVInicio-%C3%A9-obrigat%C3%B3rio-e-n%C3%A3o-est%C3%A1-preenchido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22235693626391) Tempo aproximado para leitura: **00:03:00 min****Ocorrência**Ao realizar a geração do XML do evento **S-2300** é apresentada a mensagem de erro **O campo 'matricula' do registro 'infoTSVInicio' é obrigatório e não está preenchido.**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6421206980759)

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as Versões  
  
**Causa**Este erro ocorre para o evento **S-2300 -** **Trabalhador Sem Vínculo de Emprego/Estatutário - Início**, quando o campo **Matrícula eSocial** está em branco no cadastro trabalhador. Será necessário verificar se o mesmo possui matricula, pois o preenchimento é obrigatório para vínculos enviados a partir do leiaute S-1.0.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6344556483991)

**Solução**:  
Para preenchimento da **Matrícula eSocial**, realize os passos a seguir.

1. Verifique se a [Máscara para Matricula](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013053051-RM-eSocial-Par%C3%A2metro-M%C3%A1scara-para-Matr%C3%ADcula-do-Trabalhador) foi preenchida em **Configurações | Parametrizador | eSocial | Configurações Gerais 2/7;**

![8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22235710103447)

2. Acesse o menu **eSocial | Saneamento de Dados | Preencher Matrícula eSocial;**

![oioiio.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22235710117783)

3. Selecione a coligada desejada, preencha o campo com a data de admissão caso esteja no Leiaute S-1.0, e preencha o filtro para seleção do funcionário;

![matricula.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22235693684247)

4. Após a conclusão do processo, o campo **Matrícula eSocial** no cadastro do funcionário será atualizado com a nova matricula informada no processo anterior.

![10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22235710150423)

**Observação**O campo **Gerar matrícula para funcionário sem vinculo com admissão a partir de** foi criado para atender as novas regras do leiaute S-1.0. A **data preenchida padrão será a data de alteração para o leiaute S-1.0** na base de dados. Poderá ser preenchida com uma **data igual ou superior a data padrão**. Para funcionários sem vinculo que foram transferidos será considerado a data de transferência.  
  
**Importante**  
Os Funcionários sem vínculo configurados no sistema no leiaute 2.5, a **Matrícula eSocial** não é preenchida por não ser obrigatória neste leiaute. Contudo, com a obrigatoriedade do S-1.0, a matrícula passa a ser obrigatória no XML para todos os funcionários. O sistema, porém, **não permite o preenchimento da matrícula para o funcionário cadastrado antes da utilização do leiaute S-1.0**, sendo necessário então excluir o cadastro do funcionário do sistema e cadastrá-lo novamente, **ou** realizar a inserção da matrícula via banco de dados (script de inserção não faz parte do escopo do suporte).
