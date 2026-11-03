---
article_id: 6517666765591
category: Meu RH - Gestor
content_hash: 550553356247f266cecd623f3844142caaa9f064bb0b391283ecbdb5c292c5d9
fetched_at: '2026-06-28T22:47:32.367231+00:00'
product: rm
section_id: 1500000861742
source: central-rm
title: RH - RM - Meu RH- Subordinados não aparecem para o Gestor
type: support-article
updated_at: '2026-06-01T14:24:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6517666765591-RH-RM-Meu-RH-Subordinados-n%C3%A3o-aparecem-para-o-Gestor
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22209521892119) Tempo aproximado para leitura: **00:07:52min**  
  
**Ocorrência**  
Ao acessar o menu Minha equipe do Meu RH, alguns funcionários específicos não são listados na visão do gestor.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH - Todas as versões  
  
**Causa**  
Este incidente geralmente acontece por inconsistências cadastrais ou filtros incorretos.  
  
**Solução**

Para garantir que todos subordinados sejam listados corretamente, siga os passos abaixo:

1. Aplique o filtro **"Ver todos os colaboradores"** em busca avançada, pois caso o subordinado seja indireto, ele será carregado quando esta opção marcada.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28310389254039)

Para informações detalhadas sobre este conceito, consulte:

[RH - RM - Meu RH - Explicação do conceito de subordinados diretos e indiretos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418577219735-RH-RM-Meu-RH-Filtro-funcion%C3%A1rios-diretos-e-indiretos)

**Importante: A** visualização é carregada por padrão (default), exibindo apenas os subordinados diretos. Esse comportamento também está relacionado a questões de performance do sistema.  
   
Em geral, gestores, coordenadores e cargos similares costumam realizar a conferência de ponto apenas de seus subordinados diretos, enquanto os subordinados indiretos já possuem um líder responsável por essa validação.  
   
Dessa forma, por uma questão de usabilidade e performance, os subordinados diretos são exibidos como padrão na tela inicial.  
   
Portanto, caso seja necessário realizar ações envolvendo subordinados indiretos, é importante orientar que o usuário acesse o filtro e selecione a opção para visualizar todos os subordinados (diretos e indiretos).

2. Caso os subordinados sejam de outras coligadas, deverá marcar a flag "**Considerar subordinados de todas as coligadas ..."** no grupo de quiosque do Gestor. Acesse: **Folha de Pagamento** | **Configurações | Parametrizador | RM Portal |** Selecione o código do grupo utilizado  pelo gestor,  clique em Parametrizar | **Supervisores**. 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28310379617815)

3. Verifique se o usuário do gestor ou seus perfis associados possuem filtros aplicados na tabela **PFUNC.**Caso tenha, remova todos ou ajuste os filtros para que os subordinados não listados se enquadrem na expressão utilizada. Para informações sobre como criar filtros, acesse:

[RH - RM - Meu RH - Como definir quais tipos de funcionários aparecerão em Gestão de Time](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403547339927-RH-RM-Meu-RH-Como-definir-quais-tipos-de-funcion%C3%A1rios-aparecer%C3%A3o-em-Gest%C3%A3o-de-Time)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28310379624343)

Para verificar de forma ágil se o usuário do gestor ou perfis associados possuem filtros de exibição, utilize as seguintes consultas SQL:

**Filtro no usuário:**

```
SELECT * FROM GFILTROUSUARIO WHERE CODUSUARIO = 'XXX' ---Substituir o 'XXX' pelo login
```

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28310379627287)

**Filtro no Perfil:**

```
SELECT U.CODCOLIGADA, U.CODUSUARIO, F.CODSISTEMA, F.CODPERFIL, F.TABELA, F.IDFILTRO
FROM GUSRPERFIL U
INNER JOIN GFILTROPERFIL F 
ON U.CODSISTEMA = F.CODSISTEMA AND U.CODPERFIL = F.CODPERFIL
WHERE F.TABELA = 'PFUNC' 
AND U.CODUSUARIO = 'XXXX' ---Substituir o 'XXX' pelo login
```

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28310389284247)

Após alterações nos filtros, aguarde cerca de 15 minutos ou reinicie os serviços Host e IIS para validação imediata.

4. Verificar inconsistências cadastrais:

4.1. O colaborador não será apresentado no Meu RH caso tenha inconsistências cadastrais, como por exemplo, erros no histórico de salário. Para que ele seja listado corretamente, é necessário corrigir essas pendências. Para realizar esta conferência, acesse o módulo **Folha de Pagamento | Folha Mensal | Validações | Validação da base de dados**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28310379635863)

Execute a rotina para as chapas que não estão sendo listadas ao Gestor utilizando a **Seleção de Funcionários**:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6517590931607)

A rotina irá retornar o log informando quais são as pendências desse funcionário para serem ajustadas:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6517725438871)

4.2 Caso esteja marcado o parâmetro "**Exibir Subordinados demitidos com rescisão não calculada**" no grupo de Quiosque do gestor, deverá avaliar na tabela **PFUNC** se o campo **RESCISAOCALCULADA** da chapa do subordinado está com o valor **0** ou **1.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28310389294871)

Caso o valor esteja **NULL**, deverá solicitar ao DBA da empresa para atualizar o valor do campo para "**0**" (Rescisão não calculada) ou "**1**" (Rescisão calculada) via banco de dados. Caso a modificação deste campo não seja realizada, mantenha o parâmetro desmarcado para garantir que o subordinado seja listado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28310379642775)

Consulta SQL para verificar:

```
SELECT RESCISAOCALCULADA FROM PFUNC WHERE CHAPA = 'XXX'
```

Seguindo esses passos, o problema deverá ser resolvido e os subordinados passarão a ser exibidos corretamente no Meu RH. Caso as orientações não solucionem a situação, entre em contato com o suporte TOTVS para assistência adicional.
