---
article_id: 360059356113
category: RH - Ambiente
content_hash: e3bd8a38861af535334952f51091d995d6876e2529e31ba2354e23734ec4f7a1
fetched_at: '2026-06-28T22:43:09.590780+00:00'
product: protheus
section_id: 20669342808471
source: central-protheus
title: RH - Linha Protheus - GPE - Como restringir um campo para usuários
type: support-article
updated_at: '2025-07-28T18:33:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059356113-RH-Linha-Protheus-GPE-Como-restringir-um-campo-para-usu%C3%A1rios
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26821512379287) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Como restringir um campo para determinados usuários?

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**No **cadastro de Usuários**, é possível configurar o **nível de acesso aos módulos** do sistema para que seja validado se este usuário tem algum tipo de **restrição de acesso**.  
Por padrão, os níveis de acesso dos módulos é 5, assim como os níveis dos campos no dicionário de dados.  
\*\*Cabe ressaltar que restrições para campos de preenchimento obrigatórios não são validadas.  
  
Para criar uma restrição por nível de campo, basta seguir os passos abaixo:  
**1.** Acesse o **Configurador > Usuário > Senhas > Usuários** OU **Grupos**.  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9931065340951)  
  
**2.** Selecione o usuário/grupo e clique em **Alterar**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9931085908631)  
  
**3.** Neste exemplo, o usuário tem acesso liberado ao SIGAGPE com Nível 5:  
Acesse a aba **Restrições de Acesso > Ambientes,** selecione no Módulo e na coluna **Nível** clique duas vezes no campo para alterar o Nível do usuário (Ex: Nível = 5)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33772859976855)  
**4.** Após alteração clique em **Confirmar.** **\*\***Os níveis de usuário servem para você controlar a visualização de campos que os usuários podem ou não possuir. Os níveis vão de **1 a 9**.   
Por exemplo, se um usuário possui **Nível 5**, no módulo GPE, ele visualizará campos que tenham nível menor ou igual a 5. Caso um campo tenha nível maior ou igual a 6, esse campo não será visualizado para o usuário.

**IMPORTANTE: isso não vale para campos obrigatórios. Campos obrigatórios irão sempre ser visualizados.**

Para configurar os níveis de usuário e dos campos, siga o procedimento abaixo:

**Atenção**: No exemplo, iremos configurar determinado campo para que ele não apareça na rotina para este usuário, pois o campo terá um nível maior do que o nível que está configurado para o usuário.

**Para alterar o Nível do Campo**  
  
**1.** Acesse **Configurador** > **Base de Dados** > **Dicionário** > **Bases de Dados**![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9931187285015)  
  
**2.** Clique em **Dicionário de Dados**, e selecione a tabela que contém os campos que deseja configurar (EX: SRA):  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9931226906007)![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9931228901783)![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9931281548311)  
  
**3.** Clique sobre a tabela e clique em **Editar:****![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9931268721303)  
  
4.** Clique em **+Funcionários** e clique em **Campos:**![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9931307005207)  
  
**5.** Clique na **Lupa** e pesquise o campo. (EX RA\_SALARIO). Selecione o campo e clique em **Editar:**![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9931314103703)

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9931371059479)  
  
**6.** Na **aba Validações**, altere o nível do campo para um número superior ao nível do usuário (Ex.: Nível=6):  
![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9931389199383)  
  
**7.** Clique em **Salvar**, depois em **Confirmar**  
**8.** Para que, esta alteração no campo tenha efeito, é necessário atualizar a base de dados. Em **modo exclusivo** (nenhum usuário pode estar acessando as tabelas envolvidas na alteração), clique no ícone **Atualizar Base de Dados:**![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9931414056471)  
  
**9.** Clique em **Avançar** até **Finalizar,** confirmando a atualização dos campos alterados  
**10.** Conforme exemplo acima, o usuário/grupo em questão não irá visualizar o campo **RA\_SALARIO** na rotina GPEA010, ao Incluir ou Alterar um funcionário:  
![mceclip13.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9931718688151)  
 **Observações:**- Essa regra é **valida** apenas para campos que **não sejam obrigatórios**, ou seja, **campos obrigatórios não respeitam os níveis de acesso**, serão sempre exibidos;  
- O Campo Nível Global de Campos é utilizado apenas para a ferramenta Protheus *Search*.  
  
**Saber Mais:**[Pacote de Expedição Contínua - Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854)[RH - Linha Protheus - GPE - LGPD Lei Geral de Proteção aos Dados Pessoais](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406121062935-RH-Linha-Protheus-GPE-LGPD-Lei-Geral-de-Prote%C3%A7%C3%A3o-aos-Dados-Pessoais?source=search)

[RH - Linha Protheus - GPE - Restringir acesso de usuário a determinada rotina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059006033-RH-Linha-Protheus-GPE-Restringir-acesso-de-usu%C3%A1rio-a-determinada-rotina?source=search)

[RH - Linha Protheus - GPE - Como permitir que um usuário tenha acesso apenas a Funcionários Demitidos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057151373-RH-Linha-Protheus-GPE-Como-permitir-que-um-usu%C3%A1rio-tenha-acesso-apenas-a-Funcion%C3%A1rios-Demitidos?source=search)

[RH - Linha Protheus - GPE - Como restringir o acesso do usuário à alteração de campo específico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052716514-RH-Linha-Protheus-GPE-Como-restringir-o-acesso-do-usu%C3%A1rio-%C3%A0-altera%C3%A7%C3%A3o-de-campo-espec%C3%ADfico?source=search)
