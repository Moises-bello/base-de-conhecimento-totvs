---
article_id: 10468742373911
category: GPE - eSocial - Periódicos
content_hash: be7a0c869994d66286f7f2f4529fdd9484022dbd96897489a8c4235c88ce0045
fetched_at: '2026-06-28T22:45:09.103977+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2230 - Esse trabalhador iniciou o esocial
  afastado, verifique o envio do término deste afastamento
type: support-article
updated_at: '2025-07-02T19:47:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10468742373911-RH-Linha-Protheus-GPE-eSocial-S-2230-Esse-trabalhador-iniciou-o-esocial-afastado-verifique-o-envio-do-t%C3%A9rmino-deste-afastamento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19232122490263)** Tempo aproximado para leitura: **00:02:00** min  
  
**Ocorrência**  
Esse trabalhador iniciou o esocial afastado, verifique o envio do término deste afastamento  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33212777003159)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as Versões  
  
**Causa**  
Ao tentar salvar o Calculo de Férias calculada o sistema exibe mensagem **Esse trabalhador iniciou o esocial afastado, verifique o envio do término deste afastamento.  
  
Solução**Esta mensagem é apresentada quando no cadastro inicial (**evento S-2200**) do funcionário esta com 'Informações do Afastamento do Trabalhador' e não consta o S-2230 referente ao Fim do Afastamento. Existem três cenários diferentes para esse erro:  
  
Segue o procedimento para validação:

1. Acessar o cadastro do funcionário no TAF como visualização do evento S-2200 (Módulo 84: Atualizações > Eventos Esocial > Trabalhador > Cadastro Trabalhador);
2. Verifique se consta na 'Informações do Afastamento do Trabalhador' (data inicio e motivo) o afastamento: ![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10467866237463)

**Cenário 1:**O funcionários foi transferido enquanto estava afastado, levado data inicial do afastamento no S-2200 da empresa/filial destino. Porém **a data término já consta no eSocial como 'afastamento início e término'**.   
Segue o passo a passo para a correção:

1. Acessar o cadastro do funcionário no TAF como Visualizar o evento S-2200 (Atualizações > Eventos Esocial > Trabalhador > Cadastro Trabalhador)
2. Copiar o número do recibo em um bloco de notas;
3. Sair da visualização e acessar como alterar o evento S-2200 (retificar).
   * Encontrar o campo do início do afastamento e motivo no cadastro do trabalhador, e remover a informação dos campos 'Ini. Afastam.' e 'Cód. Mot. Afas.', conforme destacado na imagem abaixo;![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10467866237463)
   * Salvar o registro será gerado uma retificação do S-2200;
4. Ajustar o recibo com o número está anotado no bloco de notas: [Como realizar ajuste de recibo do eSocial no TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019678672-RH-Linha-Protheus-TAF-eSocial-Funcionalidades-Como-realizar-ajuste-de-recibo-do-eSocial-no-TAF)
5. Realize o procedimento que estava apresentando erro (cadastro de afastamento no GPE ou cálculo as férias).

Para que não aconteça com as próximas transferências, basta estar com a expedição contínua atualizada, disponível na nossa página [eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/public/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
  
  
**Cenário 2:**O funcionários foi transferido enquanto estava afastado, levado data inicial do afastamento no S-2200 da empresa/filial destino. Porém **a data término consta no GPE e eSocial como 'afastamento término', mas não consta no TAF** (Exemplo: afastamento por  auxilio doença). Segue o passo a passo para a correção:

1. Incluir o afastamento término no TAF (Atualizações > Eventos eSocial > Não Periódicos > Afastamento Temp.>> Incluir);
2. Preencher os campos 'Id. Func.', 'Id. Mot. Afast.' e 'Dt. Fim Afas.'. confirme a inclusão:**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10468994576407)![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10467965271575)**
3. Copie o numero do recibo do afastamento término no eSocial:
4. Ajustar o recibo, conforme demonstra na imagem abaixo:![](https://centraldeatendimento.totvs.com/hc/article_attachments/33212771250839)
5. Realize o procedimento que estava apresentando erro (cadastro de afastamento no GPE ou cálculo as férias).

**Cenário 3:**O funcionários foi transferido enquanto estava afastado, levado data inicial do afastamento no S-2200 da empresa/filial destino. Porém **a data término consta no GPE, mas não consta no TAF e eSocial'** (Exemplo: afastamento por auxilio doença). Segue o passo a passo para a correção:

1. Incluir o afastamento término no TAF (Atualizações > Eventos eSocial > Não Periódicos > Afastamento Temp.>> Incluir);
2. Preencher os campos 'Id. Func.', 'Id. Mot. Afast.' e 'Dt. Fim Afas.'. confirme a inclusão:**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10468994576407)**![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10467965271575)****
3. Transmitir o S-2230;
4. Realize o procedimento que estava apresentando erro (cadastro de afastamento no GPE ou cálculo as férias).

**Saiba Mais**Para saber mais consulte os *links* abaixo:  
[RH - Linha Protheus - GPE - eSocial - S-2230 - Como realizar o término do afastamento para trabalhadores que iniciaram o eSocial afastado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055462033-RH-Linha-Protheus-GPE-eSocial-S-2230-Como-realizar-o-t%C3%A9rmino-do-afastamento-para-trabalhadores-que-iniciaram-o-eSocial-afastado?source=search)   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)

Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
