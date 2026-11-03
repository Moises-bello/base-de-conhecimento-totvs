---
content_hash: 8c986dc937c2520dae21c2fae182e2a568c73a3d4f5d583863bc1c654de4f013
fetched_at: '2026-06-29T00:10:07.785107+00:00'
page_id: '452719437'
product: rm
source: tdn-rm
title: Mudança da Situação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719437
version: 3
---

Nesta etapa é configurada o motivo que será preenchida no histórico do Funcionário quando o mesmo sair e retornar de férias e a configuração e envio automático de e-mail de solicitação de férias para o Gestor  
   
**Campos e Parâmetros**  
*Mudança da Situação*  
Nos campo abaixo deve ser preenchido o motivo da mudança da situação quando o funcionário iniciar e/ou retornar de férias. Estes motivos será inseridos no registro do Histórico de situação do Funcionário.   
   
Motivo início de férias  
Informar neste campo o motivo de início de férias. O motivo deve ser previamente cadastrado na tabela dinâmica INT28 em Administração de Pessoal | Cadastro | Cadastros Globais | Tabelas Dinâmicas.  
Ao processar o Lançamento das férias, é alterado a situação do Funcionário para F, inserindo no Histórico de Situação um registro com situação = 'F' e o motivo informado neste campo.   
Quando este motivo não está cadastrado, ao fazer o lançamento das férias individual retorna a mensagem informando que o campo deve ser preenchido e não executa o processo.   
   
Motivo retorno de férias  
Informar neste campo o motivo de retorno de férias. O motivo deve ser previamente cadastrado na tabela dinâmica INT28 em Administração de Pessoal | Cadastro | Cadastros Globais | Tabelas Dinâmicas.  
Ao processar a Finalização das férias, é alterado a situação do Funcionário para A, inserindo no Histórico de Situação um registro com situação = 'A' e o motivo informado neste campo.   
Quando este motivo não está cadastrado, ao fazer Finalizar as férias individual retorna a mensagem informando que o campo deve ser preenchido e não executa o processo.

**Observação**

Se os campos acima não forem preenchidos, nos processos de Lançamento e Finalização de férias globais, não retorna nenhuma mensagem para o usuário, finalizando com sucesso os processos. Porém não é inserido no Histórico de Situação o registro da mudança de situação o que pode causar inconsistências no sistema.  
*Aprovação de Férias pelo Portal*  
Nesta etapa, será definido a configuração de envio de e-mail para o gestor aprovar as férias solicitadas pelo subordinado via portal.  
   
Habilita envio de email anônimo na geração de férias  
Com este parâmetro marcado habilita o envio de e-mail anônimo para o gestor aprovar as férias do subordinado. Quando um funcionário cadastrar uma sugestão de férias, um e-mail é enviado para o chefe aprovar.

* Endereço anônimo: Neste campo será informado um endereço de e-mail anônimo ao qual será o remetente do e-mail enviado para o gestor.
* Usuário: Neste campo será informado um usuário válido do domínio de e-mail.
* Senha: Neste campo será informado a senha do usuário acima.

URL base para link de aprovação de férias enviado por email pelo portal   
Deve conter o endereço externo Portal do cliente.

**Exemplo**  
[https://rhonline.totvs.com.br/Corpore.net](https://rhonline.totvs.com.br/Corpore.net/Login.aspx)

**Atenção:** No e-mail que o chefe receber terá um link que abre direto na tela de aprovação do funcionário que cadastrou a sugestão de férias.

**Observação**  
Para o correto envio de email, deve ser realizado a configuração nos parâmetros Globais: Ambiente | Configuração | Parâmetros | Parâmetros Globais.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Parâmetros Globais - Email

<< Retornar para **Férias**
