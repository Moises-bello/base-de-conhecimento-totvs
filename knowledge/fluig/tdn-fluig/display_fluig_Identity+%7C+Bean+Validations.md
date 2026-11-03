---
content_hash: a72bdc85d6e0469674b77fc8c17e30c73dbae2caea070a42d96b76c793ac3c65
fetched_at: '2026-06-28T21:35:23.267632+00:00'
page_id: '244726093'
product: fluig
source: tdn-fluig
title: Identity | Bean Validations
type: documentation
url: https://tdn.totvs.com/display/fluig/Identity+%7C+Bean+Validations
version: 7
---

A API Bean Validations permite incluir anotações no código que dizem como os campos serão validados pela aplicação.

Abaixo temos um exemplo de algumas anotações básicas existentes na API:

javaEclipseValidações Básicastrue

Junto com a estrutura desenvolvida no Identity, tais anotações são validadas automaticamente quando a classe ou o método possui a anotação **@ValidateParams**.

Para isso, as anotações de validação devem ser colocadas na classe de **Implementação** e também nas I**nterfaces** onde os métodos são definidos.

**A anotação @ValidateParams deve ser colocada somente na implementação**.

serviceImplementationServiceInterfacejavaEclipsetrueServiceImpljavaEclipsetrue

### Agrupamento de Validações

É possível agrupar validações em uma mesma validação personalizada, conforme exemplo abaixo, que faz várias validações em um único parâmetro.:

javaEclipseMultiplas Validaçõestrue

Para simplificar, poderíamos criar uma validação personalizada, combinando todas essas validações em uma única validação (@Plate)

javaEclipseValidações Agrupadastrue

Para isso, é necessário criar uma anotação nova, seguindo alguns padrões.

javaEclipseValidação Customizadatrue[] groups() default {};
// Área para inclusão de dados genéricos
Class[] payload() default {};
}
]]>

É possível também criar validadores customizados para as anotações.

Seguindo o exemplo acima, poderíamos incluir uma verificação no Detran, para verificar se a placa é realmente válida, para isso, é necessário escrever código para realizar essa consulta.

Com algumas modificações, é possível incluir um validador customizado para essa tarefa:

customValidatorPlatejavaEclipse@Platetrue[] groups() default {};
Class[] payload() default {};
}
]]>DetranValidatorjavaEclipseDetranValidatortrue {
private CaseMode caseMode;
@Override
public void initialize(CheckCase constraintAnnotation) {
this.caseMode = constraintAnnotation.value();
}
@Override
public boolean isValid(String object, ConstraintValidatorContext constraintContext) {
var validDetran = pesquisaDetran(); // logica de pesquisa no detran
if ( validDetran ) {
return true;
}
return false;
}
}
 ]]>
