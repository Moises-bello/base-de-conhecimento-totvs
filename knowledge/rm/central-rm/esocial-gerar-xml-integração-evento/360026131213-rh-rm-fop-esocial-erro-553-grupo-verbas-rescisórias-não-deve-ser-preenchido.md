---
article_id: 360026131213
category: eSocial - Gerar XML/ Integração Evento
content_hash: 72d46e2bcf0067cd3becba1c334605375d335d88b1a81bdce58b76bfb6e3a4be
fetched_at: '2026-06-28T22:47:12.146789+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro 553: Grupo Verbas Rescisórias não deve ser
  preenchido'
type: support-article
updated_at: '2024-12-30T15:35:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026131213-RH-RM-FOP-eSocial-Erro-553-Grupo-Verbas-Rescis%C3%B3rias-n%C3%A3o-deve-ser-preenchido
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24441921421463)**Tempo aproximado para leitura:**00:04:00 min  
  
Ocorrência**Ao enviar os eventos **S-2299** e/ou **S-2399** é retornada a mensagem de erro código 553: **Grupo #39;V****erbas Rescisórias#39; não deve ser preenchido.**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360057328673)

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões

**Causa**Este erro ocorre em três situações:

* Quando os eventos de rescisão **S-2299** e **S-2399** estão sendo enviados com verbas rescisórias porém, a geração de verbas segue a data de obrigatoriedade de eventos periódicos. Ou seja, caso a empresa ainda não esteja dentro da obrigatoriedade de eventos periódicos, deverá enviar o **S-2299/S-2399** sem as verbas rescisórias, somente com os dados da rescisão;
* Quando o motivo de desligamento é igual a 11, 12, 13, 25, 28, 29, 30, 34, 36, 43, 44;
* Ou quando o **S-2399** está sendo enviado no leiaute S-1.0 e a categoria do funcionário é diferente de **721**. Neste caso, o grupo **verbasResc** não deve ser enviado, sendo as verbas rescisórias levadas no S-1200.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24442636668439)

**Solução**

* **Data da obrigatoriedade**

1. Acesse em **Folha de Pagamento | Configurações | Parametrizador | eSocial | Configurações Gerais 1/7** e confira as datas de obrigatoriedade dos eventos periódicos conforme [Cronograma eSocial](https://www.gov.br/esocial/pt-br/noticias/adiado-o-inicio-da-fase-de-envio-de-folhas-de-pagamento-para-orgaos-publicos-e-organizacoes-internacionais).

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6849924753431)

2. Caso possua divergência, regere o XML após correção;

3. Caso esteja tudo correto e o erro persista, acione a equipe de atendimento com as evidências supracitas e o XML.

* **Motivo Desligamento**

1. Acesse **Administração de Pessoal - Funcionários - Rescisão**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24442636676503)

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/24442636685719)**

2. Verifique se o Motivo de Desligamento informado, gera no XML conforme o [Mapeamento da TOTVS](https://tdn.totvs.com/display/public/LRM/Evento+S-2299) ou conforme o [De/Para Motivo Desligamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056309114-RH-RM-FOP-eSocial-De-Para-de-afastamento-eSocial);

3. Caso necessário faça a correção e regere o XML;

4. Caso esteja tudo correto e o erro persista, acione a equipe de atendimento com as evidências supracitadas e XML.

* **S-2399 gerando com verbas rescisórias para categorias diferentes de 721**

1. A simplificação do eSocial trouxe uma importante alteração referente a geração das verbas rescisórias de funcionários sem vínculos: a partir do leiaute S-1.0, o grupo **verbasResc** (verbas rescisórias) do evento **S-2399** só deverá ser gerado para funcionários de categoria **721- Contribuinte individual - Diretor não empregado, com FGTS**. Para os demais funcionários sem vínculo, deve-se enviar o **S-2399** sem o grupo **verbasResc** e, as devidas verbas rescisórias serão geradas no **S-1200**/**S-1202**.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24442622570519)

Não é necessária nenhuma configuração adicional para geração das verbas nos corretos eventos. O sistema já irá gerar corretamente o grupo **verbasResc** no S-2399 somente para a categoria **721** e irá gerar o S-1200/S-1202 para as demais categorias.  
2. Caso o sistema esteja gerando incorretamente o XML, acione a equipe de atendimento com as evidências.

**Saiba mais**  
Para mais informações, acesse:  
     - [Contato com o Governo para dúvidas sobre os eventos do eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004050432)  
     - [Exportar arquivos XML no RM e TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018304851)  
     - [Verbas rescisórias de funcionários sem vínculo empregatício](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409629552663-RH-RM-FOP-eSocial-Verbas-rescis%C3%B3rias-de-funcion%C3%A1rios-sem-v%C3%ADnculo-empregat%C3%ADcio?source=search)
