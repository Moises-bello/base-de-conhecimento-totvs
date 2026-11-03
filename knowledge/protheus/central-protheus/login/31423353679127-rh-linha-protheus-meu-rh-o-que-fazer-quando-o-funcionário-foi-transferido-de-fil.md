---
article_id: 31423353679127
category: LOGIN
content_hash: 4a8769b386b2b73bfc884efe491e6ed048048ade9897c9fff2b671dd94ebeacf
fetched_at: '2026-06-28T22:44:40.379414+00:00'
product: protheus
section_id: 10299559916567
source: central-protheus
title: RH - Linha Protheus - Meu RH - O que fazer quando o funcionário foi transferido
  de Filial, e perdeu o acesso ao Meu RH
type: support-article
updated_at: '2026-02-03T18:20:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31423353679127-RH-Linha-Protheus-Meu-RH-O-que-fazer-quando-o-funcion%C3%A1rio-foi-transferido-de-Filial-e-perdeu-o-acesso-ao-Meu-RH
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31423347432471) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
O que fazer quando o funcionário foi transferido de Filial, e perdeu o acesso ao Meu RH?  
  
**Ambiente**  
TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
  
**Solução**  
O Meu RH não difere filial para acesso, será sempre o mesmo *login* e senha do funcionário quando a Transferência for **somente de Filial.**  
  
Se por acaso a transferência for de Grupo de Empresa, o usuário será diferente, pois haverá outro *link* de acesso e **outro cadastro de participante.**  
  
No caso de uma transferência entre filiais no mesmo Grupo de Empresa, a **RD0 - Cadastro de Participante** precisará permanecer somente **com um registro para este funcionário**, se houver mais de um registro na RD0 **com o mesmo RD0\_CIC, apague o mais recente.**  
  
Este registro na RD0, precisará estar com o **campo Ativo = SIM (primeira aba).**  
Como o funcionário foi transferido de filial, certamente ele possui agora uma segunda matrícula na SRA deste Grupo de Empresa.  
  
O que está faltando é o relacionamento desta matrícula nova dele na SRA, com o cadastro do participante na RD0 dele, **este relacionamento é gravado na RDZ.**  
  
Como este funcionário agora, possui duas matrículas, ou seja, dois registros na SRA, **na RDZ ele vai precisar também ter dois relacionamentos**, dois registros na RDZ **apontando para o mesmo código na RD0, no campo RDZ\_CODRD0.**  
  
Este relacionamento que está faltando. Mas como criar ele?  
Na própria rotina de **Cadastro de Participantes - APDA020**, selecionará o registro deste participante, que precisa ser único e estar ativo (legenda verde), clique em **Outras Ações -> Relacionar Participante -> Atualizar,** com isso, abrirá alguns parâmetros para serem selecionados, com o intuito da criação deste relacionamento.  
  
Por fim, bastará selecionar nos parâmetros a matrícula nova deste funcionário, para que o relacionamento seja criado com base no código do participante que foi selecionado na tela anterior.  
  
Poderá ser verificado se, na tabela RDZ foi criado o vínculo corretamente, para isso filtre o campo **RDZ\_CODRD0 = (código da RD0)**, precisará ter dois relacionamentos, cada um com sua Filial + Matrícula correspondente e, os dois apontando para o **mesmo código da RD0 no campo filtrado.**  
  
Exemplo de funcionário com transferência de filial somente, mantendo o mesmo código de participante.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36163025990551)  
  
**Saiba Mais**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
