---
article_id: 360041857553
category: RH - Funcionários
content_hash: bd33b498fcf765cf5c3e68e139c204e8d262bbe93ffa0bd1c1bf6c4f08325055
fetched_at: '2026-06-28T22:43:27.294082+00:00'
product: protheus
section_id: 360011909593
source: central-protheus
title: 'RH - Linha Protheus - GPE - A chave (filial/código) não pode ser excluída,
  pois está sendo utilizada nos arquivos: RD0, RDZ, SPF e SRF'
type: support-article
updated_at: '2025-09-30T01:48:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041857553-RH-Linha-Protheus-GPE-A-chave-filial-c%C3%B3digo-n%C3%A3o-pode-ser-exclu%C3%ADda-pois-est%C3%A1-sendo-utilizada-nos-arquivos-RD0-RDZ-SPF-e-SRF
---

**Dúvida**Como posso excluir o vínculo com às tabelas relacionadas ao cadastro de admissão para seguir com a exclusão do funcionário?   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.1.27

**Solução**Para solucionar essa dúvida, realizar os seguintes passos:  
  
1. No **modulo 53 - Avaliação e Pesquisa de desempenho**, acesse o Cadastro de Participantes em **Atualizações -> Participantes -> Cadastro,** selecione a matricula e clique em **Outras Ações** -> **Excluir Vínculo:**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360056071893/mceclip1.png)

2. Ao excluir o vinculo o registro na tabela RDZ é automaticamente deletado:

![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098167974/mceclip12.png)

3. Não existindo vínculo o sistema não irá mais destacar a RDZ no log de exclusão do funcionário, apenas as tabelas RD0, SPF e SRF são destacadas agora por conta da integridade do sistema:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360056072553/mceclip5.png)

4. O próximo passo é excluir a RD0, para isso, acesse o cadastro de participantes em **Outras Ações** e **Excluir**

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055194494/mceclip6.png)

5. Ao clicar em **Confirmar,** o cadastro de participantes e o registro na RD0 serão excluídos. Perceba que em uma nova tentativa de exclusão do funcionário na SRA, o sistema não gerou a mensagem referente a tabela RDZ e RD0:

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100420933/mceclip7.png)

A crítica ocorreu somente sobre às tabelas **SRF – Férias / SPF** – **Transferência de Turno**. O próximo passo é realizar o processo de exclusão dos dados destas tabelas.

6. No **modulo de Gestão de Pessoal** acesse a rotina de Transferência de Turnos em **Atualizações -> Ponto Eletrônico -> Trocas de Turno**, selecione a matricula e clique em **Outras Ações** e **Excluir**:

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055195394/mceclip8.png)

7. Por ultimo ainda no **modulo de Gestão de Pessoal** em **Atualizações -> Funcionário -> Controle Dias de Direito**: abra o cadastro como **Alterar** e clique em **Delete** posicionado na linha

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098165714/mceclip2.png)

8. Depois destes procedimentos, será possível excluir o funcionário em **Atualizações -> Funcionários -> Funcionários:**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100420493/mceclip3.png)

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100421233/mceclip8.png)  
  
Ao abrir a tela do cadastro, para efetivar a exclusão, clique em **Confirmar**

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100421253/mceclip9.png)
